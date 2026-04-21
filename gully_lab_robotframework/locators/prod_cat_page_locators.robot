*** Variables ***
${PRODUCT}  xpath=(//x-grid[@id="ajaxSection"]/x-cell)[1]
${GENDER_MALE}  xpath=//div[@class="gender-button"]/a[text()="MEN"]
${SIZE_7}  xpath=//label[@for="template--25420726337820__main-2-1"]
${QUANTITY}  xpath=//input[@id="Quantity-template--25420726337820__main"]
${ADD_TO_CART}  xpath=//button[@id="ProductSubmitButton-template--25420726337820__main"]
${QUANTITY_DEC}  xpath=//section[@id="Quantity-Form-template--25420726337820__main"]//button[1]
${QUANTITY_INC}  xpath=//section[@id="Quantity-Form-template--25420726337820__main"]//button[2]