#!powershell

$html = get-content c:\inetpub\wwwroot\iisstart.htm

$new = $html -replace "world", "Lewis"

echo $new

set-content c:\inetpub\wwwroot\iisstart.htm $new
