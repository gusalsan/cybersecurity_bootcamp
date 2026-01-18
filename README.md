# CYBERSECURITY BOOTCAMP

## MODULO 1: CRIPTOGRAFIA
  
La práctica abarca conceptos clave de criptografía simétrica y asimétrica, gestión segura de claves, hashing, HMAC, JWT, firmas digitales, derivación de claves y análisis de bloques TR31.

El objetivo fue aplicar conocimientos teóricos a problemas prácticos reales, demostrando comprensión de confidencialidad, integridad, autenticación y protección contra ataques comunes.

### Ejercicios resueltos

1. **Disociación de claves con XOR**
   - Clave fija en código: `B1EF2ACFE2BAEEFF`  
   - Clave final deseada en desarrollo: `91BA13BA21AABB12`  
   - Valor introducido por Key Manager en properties: `20553975c31055ed`  
   - En producción (clave dinámica: `B98A15BA31AEBB3F`): clave final en memoria = `8653f75d31455c0`  

2. **Descifrado AES/CBC/PKCS7**  
   - Cifrado proporcionado: `TQ9SOMKc6aFS9SIxhfk9wT18UXpPCd505Xf5J/5nLI7Of/o0QKIWXg3nu1RRz4QWElezdrLAD5LO4USt3aB/i50nvvJbBiG+le1ZhpR84ol=`  
   - IV: ceros (`00...00`)  
   - Texto en claro: "Esto es un cifrado en bloque típico. Recuerda, vas por el buen camino. Ánimo."  
   - Padding añadido: 1 byte  
   - Cambio a padding X923: funciona igual (coinciden en 1 byte)

3. **Cifrado con ChaCha20**  
   - Texto: "KeepCoding te enseña a codificar y a cifrar"  
   - Clave keystore: `af9df30474898787a45605ccb9b936d33b780d03cabc81719d52383480dc3120`  
   - Nonce: `9Yccn/f5nJJhAt2S`  
   - Propuesta de mejora para integridad: usar **ChaCha20-Poly1305** (AEAD) para confidencialidad + autenticación

4. **Análisis y ataque a JWT**  
   - Algoritmo de firma: **HS256**  
   - Body original: usuario normal  
   - JWT malicioso: intenta escalar privilegios cambiando `"rol": "isNormal"` → `"rol": "isAdmin"`  
   - Validación con pyjwt falla sin la clave secreta ("Con KeepCoding aprendemos")

5. **Hashing con SHA3 y SHA2**  
   - SHA3-256 (Keccak) del texto: `bced1be95fbd85d2ffcce9c85434d79aa26f24ce82fbd4439517ea3f072d56fe`  
   - SHA2-512 del mismo texto: `4cec5a9f85dcc5c4c6ccb603d124cf1cdc6dfe836459551a1044f4f2908aa5d63739506f6468833d77c07cfd69c488823b8d858283f1d05877120e8c5351c833`  
   - Efecto avalancha: un punto final cambia completamente el hash

6. **HMAC-SHA256**  
   - Texto + clave keystore → HMAC: `857d5ab916789620f35bcfe6a1a5f4ce98200180cc8549e6ec83f408e8ca0550`

7. **Almacenamiento seguro de contraseñas**  
   - Por qué SHA-1 y SHA-256 simples son malas opciones  
   - Mejoras: salt + pepper  
   - Recomendación final: KDFs lentas como **PBKDF2**, **bcrypt** o **Argon2**

8. **Rediseño de API REST segura**  
   - Propuesta: **AES/GCM** (cifrado autenticado) para confidencialidad + integridad sin TLS end-to-end

9. **Cálculo de KCV (Key Check Value)**  
   - KCV(SHA-256): 3 primeros bytes del hash  
   - KCV(AES): cifrado de 16 bytes de ceros con IV ceros

10. **Firma y cifrado PGP**  
    - Verificación de firma con claves Pedro/RRHH  
    - Firma de mensaje nuevo como RRHH  
    - Cifrado asimétrico con claves públicas

11. **RSA-OAEP**  
    - Descifrado de clave simétrica empaquetada  
    - Cifrados diferentes por padding aleatorio (OAEP)

12. **AES/GCM mal utilizado**  
    - Error: reutilizar clave y nonce fijos  
    - Cifrado de texto de corrección: resultado en hex y base64

13. **Firmas digitales**  
    - PKCS#1 v1.5 con RSA  
    - Ed25519 (curva elíptica)

14. **Derivación de claves con HKDF**  
    - HKDF (SHA-512) + identificador de dispositivo → claves AES y MAC derivadas

15. **Bloque TR31**  
    - Algoritmo: AES Key Derivation Binding Method  
    - Uso: AES, Both Encrypt/Decrypt, exportable bajo clave no confiable  
    - Tipo: Symmetric Key for Data Encryption

## Herramientas utilizadas

- Python + librería `cryptography`  
- CyberChef / XOR Calculator online  
- pyjwt para JWT  
- Herramientas de keystore y PGP

  

MODULO 2: CIBERSEGURIDAD 101
📄 Auditoría WebGoat - Informe Breve

Alcance: Evaluación de seguridad básica de la aplicación vulnerable WebGoat 8.1.0 en entorno local controlado.

Hallazgos principales: Múltiples vulnerabilidades del OWASP Top 10 explotadas con éxito:

    Inyección SQL (Extracción de datos y modificación del esquema)

    Autenticación Rota (Bypass de restablecimiento de contraseña)

    XSS (Reflejado y basado en DOM)

    CSRF (Falsificación de solicitudes)

    Componentes Vulnerables (Explotación de jQuery UI 1.10.4)

Metodología: Enfoque estándar de pruebas de penetración:

    Reconocimiento (nmap, Wappalyzer, dirb)

    Explotación de Vulnerabilidades (Pruebas manuales mediante WebGoat)

    Documentación (Hallazgos técnicos y estrategias de mitigación)

Herramientas utilizadas: Burp Suite, nmap, Wappalyzer, dirb, pruebas manuales en navegador.

Conclusión clave: Demuestra cómo vulnerabilidades web básicas pueden encadenarse para comprometer una aplicación completa, resaltando la importancia crítica de la validación de entrada, mecanismos de autenticación seguros y mantener las dependencias actualizadas.





Gustavo Álvarez | @gusalsan 
Bootcamp Ciberseguridad - KeepCoding | NOVIEMBRE 2025 - JULIO 2026
