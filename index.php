<?php
require_once 'simple_html_dom.php';
// Подключаем клас для работы с файлами
require_once 'Filer.php';

// Выбираем файл для записи
$file = new Filer('./tables.html');
$file->clear();

$page = 'requests_results.html';
$data = file_get_html($page);

$table = $data->find('#contenttb');
//echo $table[0];
$file->addString($table[0]);

//
// Получили таблицу с основным контентом
//

$page = './tables.html';
$data = file_get_html($page);

$table = $data->find('table');
//echo count($table);
$kurs = 3;
$indexKursa = $kurs + 3;
echo $table[$indexKursa];
//$limitedIP->addString($table[0]);

$file = new Filer('./table.html');
$file->clear();
$file->addString($table[$indexKursa]);


/*
// Перебираем строки, пропуская первую заголовочную
for ($i = $beginReport; $i < count($tr) - 2; $i++){
	// Сохраням в массив все найденные ячейки в текущей строке
	$td = $tr[$i]->find('td');
	// Текущий ip
	//$ip = $td[2]->innertext;
	$ip = $td[2]->plaintext;
	// Трафик по текущему ip
	$trafic = $td[4]->innertext;
	// Определяем единицу измерения трафика (Гб, Мб, Кб)
	$KMG = substr($trafic, -1);
	$bytes;
	
	  if ($bytes > $limit){
		  if(!(in_array($ip, $vip))){
			  $limitedIP->addString($ip);
		  }
		}
}*/
?>