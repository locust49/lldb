import lldb

def ft_reverse(debugger, command, result, internal_dict):
	mot = debugger.GetSelectedTarget()
	if mot:
		new = "FT_" + str(mot)[::-1]
		print(new)
	else:
		print("Error: No Target Selected")

def __lldb_init_module(debugger, internal_dict):
	debugger.HandleCommand('command script add -h "reverse the name of the program and add "FT_" at its beginning" -f reverse.ft_reverse reverse');
