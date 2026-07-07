# Análisis forense financiero integral — Fiat, criptoactivos y capa tributaria (LA/FT)

> Módulo condicional de la fase 7. Cárgalo cuando el caso presente flujo de fondos, trazabilidad bancaria, criptoactivos, lavado de activos (Ley 19.913), delitos tributarios (art. 97 Código Tributario) o discrepancias entre patrimonio declarado y flujos reales. El análisis cruza tres capas: **cartolas bancarias (fiat)**, **criptoactivos** e **información tributaria chilena (SII)**.

## 1. Reglas epistémicas específicas del módulo

1. El análisis detecta **indicios y patrones**, jamás emite juicios de culpabilidad. Vocabulario obligatorio: «posible indicio», «inconsistencia relevante», «patrón que merece profundización», «discrepancia que requiere explicación documental».
2. Distingue siempre, de forma expresa, entre **economía de opción o elusión** (planificación dentro de la legalidad, sin perjuicio de la norma general antielusión), **evasión** (infracción tributaria, eventualmente delito del art. 97 CT) y **lavado de activos** (art. 27 Ley 19.913, que exige delito base). La misma discrepancia puede admitir explicaciones en cualquiera de los tres niveles; el informe debe consignar todas las hipótesis compatibles y la evidencia que las discriminaría.
3. Toda tipología o señal de alerta invocada debe indicar su fuente (XI Informe de Tipologías UAF, guías GAFILAT, señales de alerta UAF) o marcarse «pendiente de verificación contra la fuente». No atribuyas a un documento oficial contenido no verificado.
4. Los montos se consignan con moneda, fecha y documento de respaldo (cartola, foja, hash de transacción, folio de formulario). Sin respaldo identificable, el dato se marca como no acreditado.

## 2. Capa 1 — Flujos fiat (cartolas bancarias)

**Insumos**: cartolas y extractos bancarios (PDF/CSV), comprobantes de transferencia, estados de tarjetas.

**Metodología**: (a) consolidación cronológica de todos los movimientos por cuenta y titular; (b) clasificación por contraparte, canal (transferencia, efectivo, cheque, tarjeta) y naturaleza aparente; (c) reconciliación ingresos/egresos por período; (d) contraste patrimonio-estilo de vida (*lifestyle-income*): coherencia entre egresos observados y fuentes de ingreso conocidas.

**Patrones de alerta en fiat** *(catálogo indicativo, verificar contra señales UAF)*: fraccionamiento de depósitos bajo umbrales de reporte (estructuración); cuentas de paso con abonos y retiros casi simultáneos sin retención de saldo; alto volumen de efectivo incompatible con el giro; transferencias reiteradas a terceros sin relación comercial o familiar acreditada; triangulación entre cuentas del mismo grupo de personas o sociedades; abonos desde múltiples ordenantes no relacionados; incoherencia entre giro declarado y contrapartes reales.

## 3. Capa 2 — Criptoactivos

**Insumos**: exports de exchanges (CSV), direcciones de wallets, historiales on-chain, comprobantes de compra/venta P2P.

**Metodología**: (a) inventario de wallets y cuentas de exchange atribuibles al sujeto, con el fundamento de cada atribución (registro KYC, transferencia desde cuenta bancaria propia, incautación de dispositivo); (b) reconstrucción del circuito: origen fiat → adquisición → movimientos on-chain → liquidación o permanencia; (c) conciliación de rampas de entrada y salida contra las cartolas de la capa 1.

**Patrones de alerta en cripto** *(catálogo indicativo, verificar)*: uso de mezcladores o servicios de anonimización; saltos entre cadenas (*chain-hopping*) sin lógica económica; conversión inmediata a *stablecoins* y dispersión en múltiples wallets; operaciones P2P en efectivo; volúmenes incompatibles con los ingresos declarados; adquisiciones financiadas desde cuentas de terceros; permanencia en exchanges sin regulación o sin KYC.

**Advertencia**: la atribución de una wallet a una persona es una **inferencia** cuya solidez depende del fundamento; consígnala siempre con su nivel de certeza conforme al principio epistémico rector.

## 4. Capa 3 — Información tributaria chilena (SII)

**Insumos**: declaraciones de renta (F22), declaraciones mensuales (F29), boletas de honorarios electrónicas (BHE), facturación electrónica emitida y recibida, libros contables, observaciones o liquidaciones del SII, información de regímenes especiales (Pro Pyme u otros).

**Metodología**: (a) reconstrucción de la posición tributaria declarada por período (ingresos, gastos, créditos y débitos de IVA, retiros); (b) contraste con los flujos reales de las capas 1 y 2; (c) examen de la cadena de facturación: sustancia económica de proveedores y clientes relevantes.

**Patrones de alerta tributarios** *(catálogo indicativo; encuadre penal en art. 97 N° 4 CT — verificar texto vigente)*:

- **Discrepancia declarado/real**: ingresos bancarios o cripto significativamente superiores a lo declarado en renta; egresos incompatibles con la renta líquida declarada.
- **Gasto ficticio y crédito indebido**: gastos deducidos sin correlato en cartolas; créditos de IVA elevados o devoluciones frecuentes sin operaciones reales verificables; facturación recibida de sociedades sin sustancia (sin trabajadores, sin domicilio operativo, sin actividad visible, constitución reciente y facturación inmediata de alto volumen).
- **Estructuras**: sociedades instrumentales o testaferros que facturan servicios inexistentes para extraer fondos; cadenas de sociedades que generan créditos fiscales artificiales; uso de BHE o facturas para justificar retiros que luego alimentan circuitos cripto o de efectivo.
- **Señales combinadas de las tres capas**: régimen tributario preferente con operaciones de alto valor incoherentes; compras de criptoactivos financiadas con recursos que no aparecen como ingresos gravados; cambios abruptos del nivel de facturación o del régimen sin justificación económica; discrepancia entre el giro declarado y las contrapartes reales observadas en cartolas o blockchain.

## 5. Cruce integral — matriz de coherencia

El producto central del módulo es la **matriz de coherencia entre lo declarado y lo observado**, por período tributario:

| Período | Ingresos declarados (F22/F29) | Abonos fiat observados | Flujos cripto atribuidos | Brecha | Explicaciones compatibles (elusión / evasión / lavado / lícita no gravada) | Diligencia discriminante |
|---|---|---|---|---|---|---|

Cada brecha relevante se desarrolla en prosa conforme a la secuencia: contexto → antecedente → respaldo verificable → norma aplicable → análisis → consecuencia jurídica → cierre. Las brechas jamás se presentan como conclusión de ilicitud: se presentan como inconsistencias que exigen explicación, con la diligencia concreta que permitiría discriminarlas (facturas de soporte, trazabilidad on-chain de wallets determinadas, verificación de sustancia de proveedores, oficios al SII, levantamiento de secreto bancario conforme al procedimiento legal).

## 6. Encuadre normativo del módulo

Verificar en cada caso, conforme a `references/marco-legal.md` o con la marca de pendiente: Ley 19.913 (art. 27, lavado de activos; autolavado; comiso), art. 97 Código Tributario (en especial N° 4, declaraciones maliciosamente falsas, facturas falsas y devoluciones indebidas) como delito base idóneo, Ley 21.595 (régimen de delitos económicos, comiso de ganancias), Ley 20.393 (responsabilidad penal de la persona jurídica), y normativa UAF sobre reporte de operaciones sospechosas. Si la perspectiva es defensiva, el mismo catálogo se examina en espejo: suficiencia del delito base, dolo, atribución de las operaciones y licitud de origen alternativa.

## 7. Formato de entrega

El informe del módulo se integra a la estructura general de la skill (sección 6 del SKILL.md), con el siguiente desarrollo interno del capítulo financiero:

1. Resumen ejecutivo integral de hallazgos.
2. Perfil del sujeto y contexto económico-tributario (giro, régimen, actividad declarada).
3. Análisis de flujos fiat.
4. Análisis de flujos de criptoactivos.
5. Análisis tributario y coherencia con los flujos reales.
6. Inconsistencias y patrones integrados (matriz de coherencia y su desarrollo).
7. Nivel de riesgo global, con justificación indicio por indicio.
8. Diligencias de profundización, priorizadas por capa.
9. Observaciones y limitaciones del análisis (información faltante, supuestos, atribuciones inferenciales).

## 8. Integración con el auto-aprendizaje

Los patrones y tipologías que resulten validados en casos concretos se capturan mediante el Protocolo de Cierre y Aprendizaje (sección 15 del SKILL.md), bajo las categorías `Tipología-LAFT` o `Tributario`, registrando **el patrón abstracto y su fuente de verificación, jamás datos de personas o causas**. Este módulo no mantiene memorias separadas: la memoria única de `references/aprendizajes.md` concentra todo aprendizaje, preservando la higiene y la trazabilidad del sistema.
