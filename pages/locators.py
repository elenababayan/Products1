from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN = (By.CLASS_NAME, "ButtonStyled__ButtonChildrenWrapper-sc-1w8q6ko-1.HvJhf")
    PHONE = (By.CSS_SELECTOR, "EnterPhone__PhoneEnterInput-frkwr9-3.hyCJl")
    SMS = (By.CLASS_NAME, "styled__CodeInput-sc-1s2j4t5-4.ijkoK")

class SearchLocators():
    SEARCH = (By.CLASS_NAME, "Input__StyledInput-uek8rt-2.lmBbYo.SearchInput__InputStyled-qo0zos-1.cpgCIZ")
    OPTION = (By.CLASS_NAME, "Box-l1l2g5-0.jFDRUz.Flex__FlexStyled-ik4kto-0.gIbhOW.ListCard__Container-sc-15x5qnx-3.hXvcwh.Product__ProductListCardStyled-azup3c-1")
    BUTTON = (By.CLASS_NAME, "ButtonStyled-sc-1w8q6ko-0.kKgRGZ.ThemedButton__StyledButton-sc-1mw9lg8-0.TGEBg.SearchInput__IconButton-qo0zos-3.cCNQse")
