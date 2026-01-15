<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:template match="/">
    <html lang="es">
      <body>
        
        <table border="2">
          <tr>
          <th colspan="3">Nuestras Bebidas</th>
          </tr>
          <tr>
            <th>Nombre</th>
            <th>Precio</th>
            <th>Tipo</th>
          </tr>
          <xsl:for-each select="menu/bebida">
          <tr>
            <td> <xsl:value-of select="nombre" /> </td>
            <xsl:choose>
                <xsl:when test="precio &gt; 2">
                    <td><em> <xsl:value-of select="precio" /></em></td>
                </xsl:when>
                <xsl:otherwise>
                    <td> <xsl:value-of select="precio" /> </td>
                </xsl:otherwise>
            </xsl:choose>
            <td> <xsl:value-of select="tipo" /></td>
          </tr> 
          </xsl:for-each>
        
        </table>
        
      </body>
    </html>
  </xsl:template>


</xsl:stylesheet>
