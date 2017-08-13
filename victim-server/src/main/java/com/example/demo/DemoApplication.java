package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import javax.validation.Valid;

@SpringBootApplication
@Controller
public class DemoApplication {
    private static long requestsCounter = 0;

    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }

    @GetMapping()
    public String greeting(@RequestParam(value = "name", required = false, defaultValue = "World") String name, Model model) throws InterruptedException {
        model.addAttribute("name", name + ++requestsCounter);
        Thread.sleep(150);//emulate some latency
        return "greeting";
    }

}
