package com.internship.tool.controller;

import com.internship.tool.client.AiServiceClient;
import com.internship.tool.dto.AiResponse;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/ai")
public class AiTestController {

    @Autowired
    private AiServiceClient aiServiceClient;

    @GetMapping("/test")
    public AiResponse testAi(
            @RequestParam String text
    ) {

        return aiServiceClient.callAi(text);
    }
}