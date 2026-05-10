package com.internship.tool.client;

import com.internship.tool.dto.AiResponse;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.*;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.HashMap;
import java.util.Map;

@Service
public class AiServiceClient {

    @Autowired
    private RestTemplate restTemplate;

    private final String AI_URL =
            "http://localhost:5000/test";

    public AiResponse callAi(String text) {

    try {

        Map<String, String> requestBody = new HashMap<>();
        requestBody.put("text", text);

        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);

        HttpEntity<Map<String, String>> request =
                new HttpEntity<>(requestBody, headers);

        ResponseEntity<AiResponse> response =
                restTemplate.postForEntity(
                        AI_URL,
                        request,
                        AiResponse.class
                );

        return response.getBody();

    } catch (Exception e) {

        System.out.println("AI Service Error: "
                + e.getMessage());

        return null;
    }
    }
}