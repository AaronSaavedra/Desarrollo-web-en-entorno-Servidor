<html>
	<body>
		<h1>Jubilación</h1>
		<?php
			function edad_en_5_años($edad) {
				return $edad + 5;
			}
			function mensaje($edad){
				if(edad_en_5_años($edad)>65){
					return "En 5 años tendrás edad de jubilación";
				} else{
					return "Disfruta de tu tiempo";
				}
			}
		?>
		<table>
			<tr>
				<th>Edad</th>
				<th>Info</th>
			</tr>

			<?php
				$lista=array(12,34,65,40,50);
				foreach ($lista as $valor) {
					echo "<tr>";
					echo "<td>".$valor."<td>";
					echo "<td>".mensaje($valor)."</td>";
					echo "<tr>";
				}
			?>
		</table>
	</body>
</html> 
