from main import main
from data import task_selection
import openpyxl
from complete_bust.complete_bust import cutting_off_excess

ABC = ['A', 'B','C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        'AA', 'AB','AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI', 'AJ', 'AK', 'AL', 'AM', 'AN', 'AO', 'AP', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AV', 'AW', 'AX', 'AY', 'AZ',
        'BA', 'BB','BC', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BK', 'BL', 'BM', 'BN', 'BO', 'BP', 'BQ', 'BR', 'BS', 'BT', 'BU', 'BV', 'BW', 'BX', 'BY', 'BZ',
        'CA', 'CB','CC', 'CD', 'CE', 'CF', 'CG', 'CH', 'CI', 'CJ', 'CK', 'CL', 'CM', 'CN', 'CO', 'CP', 'CQ', 'CR', 'CS', 'CT', 'CU', 'CV', 'CW', 'CX', 'CY', 'CZ',
        'DA', 'DB','DC', 'DD', 'DE', 'DF', 'DG', 'DH', 'DI', 'DJ', 'DK', 'DL', 'DM', 'DN', 'DO', 'DP', 'DQ', 'DR', 'DS', 'DT', 'DU', 'DV', 'DW', 'DX', 'DY', 'DZ',
        'EA', 'EB','EC', 'ED', 'EE', 'EF', 'EG', 'EH', 'EI', 'EJ', 'EK', 'EL', 'EM', 'EN', 'EO', 'EP', 'EQ', 'ER', 'ES', 'ET', 'EU', 'EV', 'EW', 'EX', 'EY', 'EZ']
init_popul = [1, 2, 12, 13, 123, 23]
init_popul_encod = ['Случайный', 'Случайный с контролем ограничений', 'Случайный и Случайный с контролем ограничений', 'Случайный и Жадная эвристика', 'Случайный и Случайный с контролем ограничений и Жадная эвристика', 'Случайный с контролем ограничений и Жадная эвристика']
selection = [1, 2, 3]
selection_encod = ['Одноточечный', 'Двухточечный', 'Многоточечный']
mutation = [1, 2, 3, 4, 5]
mutation_encod = ['Точечная', 'Сальтация', 'Инверсия', 'Транслокация', 'Дополнение']

repetitions_recording = 50
full_decision = cutting_off_excess()

wb = openpyxl.Workbook() 
line_count = 1
for i_p__index in range(0, 6):
    for s_index in range(0, 3):
        for m_index in range(0, 5):
            if line_count > 1:
                wb = openpyxl.load_workbook(filename = f'D:\\Dop Files\\Educational Shit\\Scientific_Work\\EGA_python\\EGA_DATA_RECORDING\\{repetitions_recording}_GENERATIONS_{str(task_selection())}.xlsx') 
            sheet = wb.active 

            combination_of_operators = sheet[line_count][0].value = f"{init_popul[i_p__index]}, {selection[s_index]}, {mutation[m_index]}"
            sheet[91][0].value = full_decision
            for j in range(0, 2*repetitions_recording):
                if j%2 == 0:
                    main_answer = main(init_popul[i_p__index], selection[s_index], mutation[m_index])
                    sheet[ABC[j+1]+str(line_count)].value = main_answer[0]
                    sheet[ABC[j+2]+str(line_count)].value = main_answer[1]
            line_count +=1
            wb.save(f'{repetitions_recording}_GENERATIONS_{str(task_selection())}.xlsx')
wb.close()