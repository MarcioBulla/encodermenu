from encoder_menu import * 


# get_integer(low_v=, high_v=, increment=, caption=, field=)
# selection(field=, choices=)
# wizard([functions])
# info(text)

# Get Integer
ex_integer = get_integer(low_v=1, high_v=9, increment=1, caption="teste Integer", field="test_interger")

# Selection
ex_selection = selection("selector", [("Black", "black"), "White", ("Red", "red")], "Title Selector")

# wizard
ex_wizard = wizard([ex_integer, ex_selection])

# info
ex_info = info("Created by:\n  Marcio Bulla\nfor:\n  LCD 2004")

# submenu
ex_submenu = wrap_menu("Title SubMenu", [("ops0", dummy), ("ops1", dummy), ("ops2", dummy), ("ops3", dummy), ("ops4", dummy), ("ops5", dummy), ("ops6", dummy), ("Back", back)])

# Main Menu
main_menu = wrap_menu("Main Menu", [("SubMenu", ex_submenu), ("Wizard",ex_wizard), ("Integer", ex_integer), ("Selection", ex_selection), ("Info", ex_info)])

# Start
main_menu()
run_menu() 




