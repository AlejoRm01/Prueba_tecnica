package com.example.demo;

import java.util.HashMap;
import java.util.Map;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/convert")
public class ConversionController {

    @GetMapping()
    public ResponseEntity<Map<String, Double>> convertirMetrosAKilometros(@RequestParam double metros) {
        double kilometros = metros / 1000.0;

        Map<String, Double> respuesta = new HashMap<>();
        respuesta.put("metros", metros);
        respuesta.put("kilometros", kilometros);

        return ResponseEntity.ok(respuesta);
    }
}