package com.edip.api.service;

import com.edip.api.model.DocumentMetadata;
import org.apache.commons.io.FileUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.data.mongodb.core.MongoTemplate;

import java.io.File;
import java.io.IOException;
import java.util.UUID;

@Service
public class DocumentService {

    @Autowired
    private KafkaTemplate<String, String> kafkaTemplate;

    @Autowired
    private MongoTemplate mongoTemplate;

    public String handleUpload(MultipartFile file) {
        try {
            String docId = UUID.randomUUID().toString();
            File localFile = new File("/tmp/" + docId + ".pdf");
            file.transferTo(localFile);

            DocumentMetadata metadata = new DocumentMetadata(docId, localFile.getAbsolutePath(), "UPLOADED");
            mongoTemplate.save(metadata);

            kafkaTemplate.send("document.uploaded", docId);
            return docId;

        } catch (IOException e) {
            throw new RuntimeException("Error uploading document", e);
        }
    }

    public DocumentMetadata fetchDocument(String id) {
        return mongoTemplate.findById(id, DocumentMetadata.class);
    }
}
