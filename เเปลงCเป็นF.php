<?php
$celsius = 35; 

echo "--- Celsius to Fahrenheit ---\n";

while ($celsius <= 50) {
    $fahrenheit = ($celsius * 1.8) + 32; 
    
    echo $celsius . " °C = " . $fahrenheit . " °F\n";
    
    $celsius += 10; 
}
?>