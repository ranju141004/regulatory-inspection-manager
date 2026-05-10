package com.internship.tool.dto;

public class AiResponse {

    private boolean success;
    private String content;
    private boolean is_fallback;

    public AiResponse() {
    }

    public boolean isSuccess() {
        return success;
    }

    public void setSuccess(boolean success) {
        this.success = success;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public boolean isIs_fallback() {
        return is_fallback;
    }

    public void setIs_fallback(boolean is_fallback) {
        this.is_fallback = is_fallback;
    }
}