#!powershell

# WANT_JSON
# POWERSHELL_COMMON

#$html = get-content c:\inetpub\wwwroot\iisstart.htm
#
#$new = $html -replace "world", "Lewis"
#
#echo $new
#
#set-content c:\inetpub\wwwroot\iisstart.htm $new

$params = Parse-Args $args;

$result = New-Object psobject @{
    win_file = New-Object psobject
    changed = $false
}

$content = ""

if ($params.content) {
  $content = $params.content
}

if ($params.mkdir) {
  mkdir $params.mkdir
}

switch ($params.action) {
  "delete" {

    Try {
    rm $params.file
    Set-Attr $result.win_file $params.file "deleted"
    $result.changed = $true
    }

    Catch {
      echo $Error
      Fail-Json $result "Error deleting file"
    }
  }
  "update" {
    set-content $params.file $content
  }
  default {
    new-item $params.file -value $content -itemtype file
  }
}


Exit-Json $result;
