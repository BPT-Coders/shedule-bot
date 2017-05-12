<?php
$kurs;
$indexGroup;
if (isset($argv[1])){
	$kurs = $argv[1];
}
else {
	$kurs = 1;
}

if (isset($argv[2])){
	$indexGroup = $argv[2];
}
else {
	$indexGroup = 2;
}

require_once 'simple_html_dom.php';
require_once 'Filer.php';



// Выдернуть из общей страницы только центральную (контентную) часть
$page = 'requests_results.html';
$data = file_get_html($page);
$tables = $data->find('#contenttb');
$table = $tables[0];

// Выдернуть таблицу для заданного курса
$tableKurs = $table->find('table');
$indexKursa = $kurs + 4;
$file = new Filer('./table.html');
$file->clear();
$file->addString($tableKurs[$indexKursa]); // Таблица для курса

// Определить завтрашний день недели
// 0 - ВС
// 6 - СБ
$date = strtotime("+1 day");
$tomorrow = date("w", $date);

if ($tomorrow == 0){
	echo 'Завтра воскресение';
	exit;
}

$indexRow = $tomorrow + 1; // Индекс строки в таблице

// Выдернуть строку на день
$page = './table.html';
$data = file_get_html($page);
$table = $data->find('tr');
$tr = $table[$indexRow]; // Строка на день

// Расписание по дню для группы
$table = $tr->find('td');
$indexGroup = 2;
$str = $table[0]->plaintext;
$str = str_replace(' ', '', $str);
$str = str_replace(chr(13), '', $str);
$str = str_replace(chr(10), '', $str);
$strToFile = $str;
$str = $table[$indexGroup]->plaintext;
$str = str_replace(' ', '', $str);
$strToFile =$strToFile.' '.$str;
$strToFile = str_replace('&nbsp;', ' ', $strToFile);
$file = new Filer('./group.html'); // Текст для отправки
$file->clear();
$file->addString($strToFile);
?>