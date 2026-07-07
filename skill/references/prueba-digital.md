# Análisis de prueba digital

> **Estado del módulo**: OPERATIVO en su componente metodológico. Las citas al
> CPP marcadas como verificadas constan en `references/marco-legal.md`
> (curatoría 2026-07-06); la Ley 21.459 consta **verificada** en
> `references/leyes-especiales.md` (curatoría 2026-07-07, idNorma 1177743,
> arts. 1–21, con los arts. 9 y 16 derogados y el art. 11 en vigencia
> diferida). Los artículos del CPP fuera del perímetro curado conservan la
> marca **«cita pendiente de verificación»**. Este módulo no contiene citas
> jurisprudenciales: los fallos sobre valor probatorio de evidencia digital se
> incorporarán solo identificados por tribunal, rol y fecha, previa
> verificación.

Carga este archivo cuando el caso involucre correos electrónicos, mensajería
instantánea, metadata, geolocalización, registros bancarios electrónicos,
redes sociales o evidencia incautada de dispositivos.

---

## I. Tipificación de la prueba digital

Identifica y categoriza la evidencia digital disponible. Cada categoría tiene
un valor probatorio y un protocolo de verificación distinto.

### A. Comunicaciones electrónicas

**Correos electrónicos**: cantidad, período, remitentes, destinatarios,
servidor (Exchange, Gmail, servidor propio) y disponibilidad de respaldo en el
servidor de origen.

**Mensajería instantánea** (WhatsApp, Telegram, Signal): dispositivo de origen
(IMEI), existencia de respaldo contemporáneo a los hechos (iCloud, Google
Drive), conversaciones críticas y mensajes específicos relevantes.

### B. Datos de geolocalización

**Historial de ubicaciones** (Google/Apple): permite situar un dispositivo en
lugares y tiempos determinados; su obtención exige autorización judicial
*(art. 222 CPP — cita pendiente de verificación; el artículo no integra el
perímetro curado del CPP)*.

**Metadata EXIF de fotografías**: fecha, hora, coordenadas GPS y modelo de
dispositivo, verificables contra el equipo incautado.

### C. Registros financieros digitales

**Cartolas y extractos electrónicos** con firma digital del banco emisor,
verificables contra el sistema oficial. **Logs de acceso a portales
bancarios**: usuario, IP, navegador, fecha, hora y acciones; permiten acreditar
quién autorizó una operación. Este bloque se integra con
`references/forense-financiero.md` cuando exista flujo de fondos.

### D. Redes sociales y plataformas

Publicaciones con marca temporal, ubicaciones etiquetadas y cambios de estado.
Valor probatorio individual medio; alto valor corroborante en convergencia con
otras fuentes.

### E. Metadata documental y de correo

**Metadata de documentos** (fechas de creación y modificación, autor, último
editor): permite detectar confecciones retroactivas. **Headers de correo**
(cadena *Received*, IP de origen, firma DKIM, registro SPF, Message-ID):
permiten autenticar origen y enrutamiento.

---

## II. Cadena de custodia digital

La eficacia procesal de la prueba digital depende del cumplimiento riguroso de
los siguientes requisitos. Verifica, respecto de cada pieza:

1. **Identificación por hash criptográfico** (SHA-256 como estándar) calculado
   al momento de la incautación, no después.
2. **Preservación del original**: todo análisis se ejecuta sobre copias
   forenses bit a bit; el original queda protegido contra escritura.
3. **Documentación de la cadena**: quién incautó, cuándo, dónde, con qué
   autorización, a quién se transfirió la custodia, qué perito analizó y en
   qué fechas, con registro de las herramientas forenses utilizadas.
4. **Hash de integridad verificable** consignado en el informe pericial y
   cotejable en cualquier momento posterior.
5. **Autenticación criptográfica** cuando la naturaleza de la pieza lo permita
   (DKIM/SPF, firma digital, marca temporal de plataforma).

Los instructivos del Ministerio Público sobre cadena de custodia de evidencia
digital deben citarse por su número y fecha una vez tenidos a la vista *(no
consta en los antecedentes examinados un oficio verificado; incorporar previa
verificación)*.

Cuando la cadena presente brechas, identifícalas expresamente, evalúa el
riesgo de exclusión por ilicitud o falta de autenticidad y propone diligencias
de refuerzo (peritaje adicional, ratificación de intervinientes).

---

## III. Autenticación e integridad por tipo de evidencia

### A. Correos electrónicos
**DKIM**: firma criptográfica del dominio emisor; su validez acredita que el
correo proviene del dominio reclamado. **SPF**: registro DNS que autoriza los
servidores de envío. **Análisis de headers**: la consistencia de la cadena
*Received* con los servidores y marcas temporales autoriza la inferencia de
autenticidad.

### B. Mensajería instantánea
**Marca temporal del respaldo** (iCloud/Google Drive), no modificable por el
usuario: si el respaldo es contemporáneo a los hechos, su valor es máximo.
**Verificación de dispositivo**: coincidencia IMEI/SIM con el equipo
incautado. **Consistencia de contenido** con declaraciones independientes.

### C. Fotografías
**EXIF** (GPS, marca temporal, modelo y serie del equipo) y **hash de la
imagen original** registrado en el informe pericial.

### D. Documentos bancarios y firmados digitalmente
**Certificado digital del emisor** verificable contra el repositorio público;
**cotejo con el sistema oficial** (banco, CMF, SII); **correlatividad de la
numeración** del documento.

---

## IV. Reconstrucción temporal integrada

Construye una cronología que integre evidencia digital y física, usando
`assets/templates/cronologia-hechos.md`. Para cada evento consigna: hora
exacta (con zona horaria), ubicación, acción, fuente de verificación, método
de autenticación y nivel de certeza. La fuerza probatoria de la reconstrucción
reside en que cada evento queda documentado por una fuente con marca temporal
automática; su calificación epistémica (acreditado / indiciario / inferencia)
es obligatoria evento por evento.

---

## V. Cotejo digital-físico (cross-referencing)

El mayor rendimiento de la prueba digital es refutatorio:

1. **Declaración del imputado vs. evidencia digital**: cada afirmación
   relevante se coteja contra registros con marca temporal; la contradicción
   acreditada es insumo directo de la matriz de contradicciones.
2. **Declaración de testigos vs. metadata**: la negación de un hecho que los
   registros documentan configura contradicción de máxima severidad.
3. **Documentos aportados vs. metadata**: la fecha de creación posterior al
   hecho que el documento pretende respaldar es indicio grave de confección
   retroactiva; su calificación jurídica (falsedad, uso malicioso) queda
   sujeta al tipo penal aplicable.

La convergencia de fuentes digitales independientes (correo, mensajería,
geolocalización, registros bancarios) constituye el patrón probatorio más
sólido disponible; consígnala expresamente en el ACH.

---

## VI. Diligencias digitales típicas

Propón, cuando el caso lo amerite y con indicación de norma habilitante,
autorización requerida y plazo realista:

1. **Incautación de dispositivos y registros** *(arts. 217 y 219 CPP — citas
   pendientes de verificación)*, con autorización judicial previa cuando la
   diligencia afecte garantías; la autorización judicial de diligencias que
   priven, restrinjan o perturben derechos del imputado o de terceros consta
   en el art. 9 CPP (verificado).
2. **Pericia computacional**: recuperación de archivos eliminados, historial
   de navegación, extracción de mensajería, análisis de metadata.
3. **Oficio a operador de telecomunicaciones** por tráfico y geolocalización
   *(art. 222 CPP — cita pendiente de verificación)*.
4. **Oficio a proveedores de servicios** (Google, Apple, Microsoft, Meta) por
   cuentas, respaldos e historial de ubicación; frecuentemente exige
   cooperación internacional.
5. **Oficio a entidades bancarias** por extractos electrónicos, logs de
   acceso y transferencias.
6. **Preservación provisoria de datos informáticos**: art. 218 bis CPP,
   introducido por la Ley 21.459; el texto de inserción consta verificado en
   el extracto de esa ley (`references/leyes-especiales.md`), sin perjuicio de
   cotejar el texto consolidado del CPP en la próxima curatoría — diligencia
   urgente por riesgo de pérdida.
7. **Captura notarial** de publicaciones públicas en redes sociales.

---

## VII. Marco normativo y de admisibilidad

- **Libertad probatoria** *(art. 295 CPP — cita pendiente de verificación)*:
  todos los hechos pueden probarse por cualquier medio producido e
  incorporado conforme a la ley.
- **Exclusión de prueba ilícita**: la exclusión por inobservancia de
  garantías fundamentales se controla en la audiencia de preparación; el
  art. 276 CPP no integra el perímetro curado *(cita pendiente de
  verificación)*, pero la nulidad procesal y el recurso de nulidad (arts.
  372–387 CPP) constan verificados en `marco-legal.md`.
- **Delitos informáticos y evidencia**: tipos (arts. 1° a 8°), reglas
  procesales y preservación de datos de la Ley 21.459, **verificados** en
  `references/leyes-especiales.md`; precaución con el art. 11 (vigencia
  diferida) y los arts. 9 y 16 (derogados).
- **Jurisprudencia**: no consta en los antecedentes examinados fallo
  verificado sobre valor probatorio de evidencia digital; toda cita se
  incorporará individualizada por tribunal, rol, fecha y considerando, previa
  verificación conforme a la sección 7 del SKILL.md.

---

## VIII. Cierre

La prueba digital con cadena de custodia íntegra y autenticación criptográfica
verificable es el medio de acreditación más sólido disponible en la
investigación moderna; su valor se pierde con la omisión de cualquier eslabón
—hash inicial, copia forense, registro de cadena, autenticación—. La
sistematización de este módulo constituye, por ello, condición de eficacia
procesal de la evidencia y no mera prolijidad metodológica. Toda afirmación
técnica que funde una conclusión jurídica debe quedar calificada
epistémicamente y, si depende de norma no curada, portar su marca «pendiente
de verificación».
