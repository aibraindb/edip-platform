package com.edip.api.model;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Document("documents")
public class DocumentMetadata {
    @Id
    private String id;
    private String filePath;
    private String status;

    public DocumentMetadata() {}

    public DocumentMetadata(String id, String filePath, String status) {
        this.id = id;
        this.filePath = filePath;
        this.status = status;
    }

    public String getId() { return id; }
    public String getFilePath() { return filePath; }
    public String getStatus() { return status; }

    public void setId(String id) { this.id = id; }
    public void setFilePath(String filePath) { this.filePath = filePath; }
    public void setStatus(String status) { this.status = status; }
}
