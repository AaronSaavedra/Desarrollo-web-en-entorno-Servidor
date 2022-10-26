<?php
	$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
?>
<html>
	<style>
		table, th, td{
			border: 1px solid black;
		}
		.tr1:hover{
			background-color: black;
		}
		.id:hover{
			color:blue;
		}
		.imagen{
			width: 100px;
			height: 50px;
			background: #008000;
			transition: width 2s, height 2s, margin 2s;
			margin: 50px auto 0;
		}
		.imagen:hover{
			width: 100%;
			height: 100px;
			margin: 0 auto;
			-webkit-transform: rotate(360deg);
			transform: rotate(360deg);
		}
	</style>
	<body>
		<h1>Conexión establecida</h1>
		<a href="/logout.php">Logout</a>	
	<table>
			<tr>
				<th>Id</th>		
				<th>Nombre</th>
				<th>Url_Imagen</th>
				<th>Autor</th>
					<th>Genero</th>
			</tr>
			<?php
			// Lanzar un query
			$query =  'SELECT * FROM tLibros';
			$result = mysqli_query($db, $query) or die('Query error');
			while ($row = mysqli_fetch_array($result)) {
				echo '<td><a href="/detail.php?id='.$row[0].'">'.$row[0].'</a></td>';
				echo '<tr>';
				echo '<td>'.$row[1].'</td>';
				echo '<td><img src="'.$row[2].'" width="100" height="100"></td>';
				echo '<td>'.$row[3].'</td>';
				echo '<td>'.$row[4].'</td>';
				echo '</tr>';
			}
			mysqli_close($db);
			?>
	</body>
</html>
