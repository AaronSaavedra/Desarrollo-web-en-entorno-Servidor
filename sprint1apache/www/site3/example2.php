<html>
	<body>
		<h1>Página de bienvenida</h1>
		<?php
			function dar_bienvenida($nombre) {
				echo "Bienvenido/a, " . $nombre . "!";
			}
			
			dar_bienvenida("Will Smith");
		?>
	</body>
</html>
