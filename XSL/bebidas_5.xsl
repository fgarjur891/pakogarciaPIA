<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:template match="/">
    <html lang="es">
      <body>
        <h2>Bebidas (Usando Templates)</h2>
        
        <ul>
        <xsl:apply-templates />
        </ul>
        
      </body>
    </html>
  </xsl:template>

  <xsl:template match="menu/bebida">
    <li>
      <xsl:value-of select="nombre"/>
    </li>
  </xsl:template>

</xsl:stylesheet>