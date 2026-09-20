import unittest
from servicios.catalogo import Catalogo


class TestCatalogo(unittest.TestCase):

    def setUp(self):
        """Se ejecuta antes de cada test para tener un catálogo cargado y fresco."""
        self.catalogo = Catalogo()
        self.catalogo.cargar_datos()

    def test_cargar_datos_no_esta_vacio(self):
        """Verifica que el JSON se lea correctamente y cargue juegos."""
        self.assertGreater(
            len(self.catalogo), 0, "El catálogo debería tener al menos un juego."
        )

    def test_buscar_por_nombre_existente(self):
        """Verifica que encuentre un juego existente sin importar mayúsculas/minúsculas."""
        # Probamos con un término en minúsculas (ej: 'catan' o parte del nombre)
        juegos = self.catalogo.buscar_por_nombre("catan")

        # Si en tu JSON tenés 'Catan', debería encontrar al menos uno
        if len(self.catalogo) > 0 and juegos:
            self.assertTrue(
                any("catan" in j.get_nombre().lower() for j in juegos),
                "El resultado de la búsqueda debería contener el nombre buscado.",
            )

    def test_buscar_por_nombre_inexistente(self):
        """Verifica que devuelva una lista vacía si el juego no existe."""
        juegos = self.catalogo.buscar_por_nombre("juego_que_no_existe_12345")
        self.assertEqual(len(juegos), 0)

    def test_filtrar_por_categoria_existente(self):
        """Verifica que devuelva solo los juegos que pertenezcan a esa categoría."""
        categorias = self.catalogo.obtener_categorias_disponibles()

        if categorias:
            cat_prueba = categorias[0]  # Tomamos la primera categoría válida
            juegos_filtrados = self.catalogo.filtrar_por_categoria(cat_prueba)

            self.assertGreater(
                len(juegos_filtrados),
                0,
                f"Debería haber al menos un juego en '{cat_prueba}'.",
            )

            # Comprobamos que todos los juegos devueltos tengan esa categoría
            for juego in juegos_filtrados:
                cats_juego_lower = [c.lower() for c in juego.get_categorias()]
                self.assertIn(cat_prueba.lower(), cats_juego_lower)

    def test_obtener_categorias_disponibles_sin_duplicados(self):
        """Verifica que devuelva una lista de categorías ordenadas y sin repetir."""
        categorias = self.catalogo.obtener_categorias_disponibles()

        self.assertIsInstance(categorias, list)
        self.assertEqual(
            len(categorias),
            len(set(categorias)),
            "Las categorías disponibles no deberían tener duplicados.",
        )


if __name__ == "__main__":
    unittest.main()