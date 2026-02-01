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

### Herramientas utilizadas

- Python + librería `cryptography`  
- CyberChef / XOR Calculator online  
- pyjwt para JWT  
- Herramientas de keystore y PGP

  

## MODULO 2: CIBERSEGURIDAD 101
**Auditoría WebGoat - Informe Breve**

**Alcance**: Evaluación de seguridad básica de la aplicación vulnerable WebGoat 8.1.0 en entorno local controlado.

**Hallazgos principales**: Múltiples vulnerabilidades del OWASP Top 10 explotadas con éxito:

    Inyección SQL (Extracción de datos y modificación del esquema)

    Autenticación Rota (Bypass de restablecimiento de contraseña)

    XSS (Reflejado y basado en DOM)

    CSRF (Falsificación de solicitudes)

    Componentes Vulnerables (Explotación de jQuery UI 1.10.4)

**Metodología**: Enfoque estándar de pruebas de penetración:

    Reconocimiento (nmap, Wappalyzer, dirb)

    Explotación de Vulnerabilidades (Pruebas manuales mediante WebGoat)

    Documentación (Hallazgos técnicos y estrategias de mitigación)

**Herramientas utilizadas**: Burp Suite, nmap, Wappalyzer, dirb, pruebas manuales en navegador.

**Conclusión clave**: Demuestra cómo vulnerabilidades web básicas pueden encadenarse para comprometer una aplicación completa, resaltando la importancia crítica de la validación de entrada, mecanismos de autenticación seguros y mantener las dependencias actualizadas.

## MODULO 3:  BLUE TEAM, montaje de una Infraestructura de Red

Esta práctica consiste en construir un laboratorio de ciberseguridad Blue Team utilizando **pfSense** como firewall/router central en VirtualBox. El objetivo es crear una red segmentada con aislamiento entre zonas (LAN, DMZ y DMZ2), desplegar servicios expuestos de forma controlada y monitorear amenazas con herramientas de detección.

### Esquema general de la infraestructura
Elastic Cloud (SIEM)
↑
Router de casa / WAN
↑
pfSense
/         |         
LAN          DMZ         DMZ2
(Windows 10)   (Apache +      (Suricata

Agente      Honeypot       o solo uno)
Elastic)      Cowrie)

- **WAN**: Conexión a Internet (adaptador puente).
- **LAN**: Red interna segura (192.168.100.0/24) → Windows 10 + agente Elastic.
- **DMZ**: Zona expuesta (192.168.200.0/24) → Servidor web Apache y/o honeypot Cowrie.
- **DMZ2**: Zona de monitoreo (192.168.250.0/24) → Suricata (IDS) o alternativa.

### Requisitos previos

- VirtualBox instalado.
- Imagen ISO de pfSense.
- Máquinas virtuales Kali Linux y Windows 10.
- Docker en Kali (para Cowrie).
- Cuenta gratuita en Elastic Cloud para SIEM.

### Instalación y configuración básica de pfSense

Descargamos la ISO de pfSense, la extraemos y creamos una nueva máquina virtual en VirtualBox (tipo BSD → FreeBSD 64-bit, 1250 MB RAM, 1 CPU, disco de 16 GB). Configuramos los cuatro adaptadores de red: Adaptador 1 en modo puente (WAN), y los otros tres en red interna con nombres “LAN”, “DMZ” y “DMZ2”.

Arrancamos la VM con la ISO montada e instalamos pfSense aceptando las opciones por defecto hasta completar la instalación. Una vez finalizada, apagamos la máquina, eliminamos la ISO del almacenamiento virtual y volvemos a arrancar. Tras un minuto deberíamos ver la consola de pfSense con las interfaces asignadas.

### Configuración inicial desde Kali en LAN

Creamos o usamos una Kali con el adaptador 1 en red interna “LAN”. Desconectamos y reconectamos el adaptador de red para que obtenga IP por DHCP. Comprobamos con `ip a` y accedemos al wizard de pfSense desde el navegador en https://192.168.1.1 (aceptamos el riesgo).

Iniciamos sesión con admin / pfsense y seguimos el asistente: nombramos el host UTM, dominio keepcoding.local, DNS 127.0.0.1 y 1.1.1.1, ajustamos la IP LAN a 192.168.100.1/24, cambiamos la contraseña y recargamos. Reconectamos el adaptador en Kali para obtener la nueva IP y volvemos a entrar con la contraseña actualizada.

### Configuración de servicios y zonas

En **Services > DNS Resolver** deshabilitamos DNSSEC y habilitamos forwarding. En **DHCP Server > LAN** definimos el rango 192.168.100.100–150, DNS y gateway adecuados. Asignamos las interfaces OPT1 y OPT2 como DMZ (192.168.200.1/24) y DMZ2 (192.168.250.1/24), habilitamos DHCP en ambas con rangos 100–150 y DNS configurados.

### Reglas de firewall y aislamiento

Creamos un alias de puertos “web” (80 y 443). En las reglas de DMZ y DMZ2 permitimos tráfico saliente HTTP/HTTPS y DNS. En LAN bloqueamos salida hacia DMZ/DMZ2. En DMZ bloqueamos acceso a LAN y a DMZ2 (y viceversa), garantizando segmentación estricta.

### Servicios desplegados

- **DMZ**: Instalamos Apache (`apt install apache2`) y/o Cowrie con Docker (`docker run -p 222:2222 cowrie/cowrie`). Creamos port-forward desde WAN puerto 80 → Apache y 222 → Cowrie.
- **DMZ2**: Desplegamos Suricata como IDS, configuramos reglas básicas y monitoreamos logs en `/var/log/suricata/fast.log`.
- **LAN**: Windows 10 con agente Elastic para recopilación de eventos.

### Integración con Elastic SIEM

Creamos políticas en Elastic Cloud para Linux (Suricata + Custom Logs para Cowrie) y Windows. Instalamos los agentes en las VMs correspondientes y creamos data views para visualizar alertas y logs centralizados.

### Notas finales

Esta infraestructura simula un entorno real con segmentación, exposición controlada y monitoreo. Los logs de Suricata, Cowrie y Windows se envían a Elastic para análisis. Para más detalles y capturas consulta el PDF original adjunto en el repositorio.



Gustavo Álvarez | @gusalsan |
Bootcamp Ciberseguridad - KeepCoding | NOVIEMBRE 2025 - JULIO 2026
