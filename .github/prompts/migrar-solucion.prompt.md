---
agent: 'agent'
description: 'Migra una solución a otro lenguaje y explica las diferencias'
---

Analiza el siguiente código seleccionado:

${selection}

Lenguaje destino:
${input:destino:Indica JavaScript o R}

Tu objetivo NO es simplemente traducir sintaxis.

1. Explica brevemente qué algoritmo implementa el código original.
2. Identifica las principales construcciones utilizadas.
3. Muestra sus equivalentes en el lenguaje destino.
4. Genera una versión equivalente manteniendo, siempre que sea posible,
   la estructura y algoritmo originales.
5. Explica las diferencias importantes entre ambos lenguajes.
6. Si existe una forma idiomática claramente diferente en el lenguaje
   destino, muéstrala aparte y explica por qué es diferente.
7. No agregues funcionalidades que no existan en la solución original.