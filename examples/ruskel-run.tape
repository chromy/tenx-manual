Source ./common.tape
Output vid.gif

Type "tenx new"
Enter
Wait

Type "tenx ctx ruskel termsize"
Enter
Wait

Type "tenx code"
Enter
Sleep 500ms
Type "iWrite a command-line tool that outputs the current terminal size"
Sleep 500ms
Escape
Type ":wq"
Enter

Wait

Sleep 3s

Type "cargo run"
Wait
Sleep 5s
