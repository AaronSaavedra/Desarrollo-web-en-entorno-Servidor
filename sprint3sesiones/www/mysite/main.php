<?php
	$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
?>
<html>
	<style>
		table, th, td{
			border: 1px solid black;
			border-collapse: collapse;
		}
		
		td{
			padding:15px;
			text-align:center;
		}

		.Color{
			background-color:blue;
		}
		tr:hover{
			background-color:#5DC1B9;
		}

		.Imagen{
			width: 100px;
			height: 100px;
			background: #f92672;
			transition: width 2s, height 2s, margin 2s;
			margin: 50px auto 0;
		}

		.Imagen:hover{
			width: 100%;
			height: 200px;
			margin: 0 auto;

		}

	</style>
	<body>
		<h1>Conexión establecida</h1>
		<a href="/logout.php">Logout</a>	
	<table>
			<tr>
				<th class="Color">Id</th>		
				<th class="Color">Nombre</th>
				<th class="Color">Url_Imagen</th>
				<th class="Color">Autor</th>
				<th class="Color">Genero</th>
			</tr>
			<?php
			// Lanzar un query
			$query =  'SELECT * FROM tLibros';
			$result = mysqli_query($db, $query) or die('Query error');
			while ($row = mysqli_fetch_array($result)) {
				echo '<td><a class="ID" href="/detail.php?id='.$row[0].'">'.$row[0].'</a></td>';
				echo '<tr>';
				echo '<td class="Nombre">'.$row[1].'</td>';
				echo '<td><img class="Imagen" src="'.$row[2].'" width="100" height="100"></td>';
				echo '<td>'.$row[3].'</td>';
				echo '<td>'.$row[4].'</td>';
				echo '</tr>';
			}
			mysqli_close($db);
			?>
	</body>
</html>
