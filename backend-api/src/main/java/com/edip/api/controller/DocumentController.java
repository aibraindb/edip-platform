package com.edip.api.controller;

import com.edip.api.model.DocumentMetadata;
import com.edip.api.service.DocumentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
@RequestMapping("/api/documents")
public class DocumentController {

    @Autowired
    private DocumentService documentService;

    @PostMapping("/upload")
    public ResponseEntity<String> uploadDocument(@RequestParam("file") MultipartFile file) {
        String id = documentService.handleUpload(file);
        return ResponseEntity.ok(id);
    }

    @GetMapping("/{id}")
    public ResponseEntity<DocumentMetadata> getDocument(@PathVariable String id) {
        return ResponseEntity.ok(documentService.fetchDocument(id));
    }
}
