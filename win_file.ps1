#!powershell

# WANT_JSON
# POWERSHELL_COMMON

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
  $params.file = $params.mkdir + $params.file
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
    Try {
      new-item $params.file -value $content -itemtype file
      $result.changed = $true
      Set-Attr $result.win_file $params.file "created"
    }
    Catch {
      Fail-Json $result "Error creating file"
    }
  }
}


Exit-Json $result;
