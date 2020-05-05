'''
Author: Ana Javed
File: WIC_Participation_Data_for_Austin_Public_Health.csv
Start date: 09/14/19

Objective: Read open data ATX data

Data website: https://data.austintexas.gov/Health-and-Community-Services/WIC-Participation-Data-for-Austin-Public-
                Health/2t4x-8jhn

Data description from website:

        The WIC (Women, Infants and Children) Special Supplemental Nutrition program is a federal assistance program
        managed by the federal government, specifically the US Food and Nutrition Services part of the Department of
        Agriculture. This program targets low-income or nutritionally at-risk populations of women, infants and children
         to provide supplemental food benefits. First established in 1972 as a two year pilot, the program was
         permanently established in 1975 and now serves around 53 percent of infants born in the United States.

        This dataset shows monthly WIC participation data for Austin Public Health since October 2013, with variables
        such as Total Women, Total Infants and General Admin Money.

Work in Progress Notes:
    - Perhaps want to add Austin total population data as a comparison?
    - Perhaps want to add SNAP dataset to compare totals?
    - Perhaps want to add infant maternal mortality dataset? << Would only work if the dates line up

    ** To show more meaning in the data, want to see how the $$ for snap / WIC / etc. has changed over time.
        Ideally more funding to these services = more enrollees = less infant mortality?

        Gotta see how we can combine the different datasets...
        And start thinking about how to visualize & show the data


'''

import csv
import datetime


file_path = 'WIC_Participation_Data_for_Austin_Public_Health.csv'


def read_data(file_path):
    data_file = csv.reader(open(file_path), delimiter=',')

    data_dict = {}  # Reading file into here
    mother_dict = {}
    child_dict = {}

    for each in data_file:
        if each[1].strip() in ['Total Participants', '', None]:
            continue

        ### Validating index
        # for i, val in enumerate(each):
        #     print(i, val)   # confirming index
        #
        # # break

        mo_day_yr = each[0][:10].strip()                      # '01/01/2014' - '06/01/2018' range
        mo_yr = mo_day_yr[:3] + mo_day_yr[-4:]                # '01/2014'

        total_participants = each[1].strip()

        preg_women = each[2].strip()
        full_BF_women = each[3].strip()
        partial_BF_women = each[4].strip()
        PP_women = each[5].strip()
        total_women = each[6].strip()

        full_BF_infant = each[7].strip()
        partial_BF_infant = each[8].strip()
        full_formula_infant = each[9].strip()
        total_infants = each[10].strip()
        total_children = each[11].strip()

        admin_money = each[12].strip()   # float, two decimal places
        dshs_source = each[13].strip()   # PDF source to the data -- < not sure we need this, skipping for now


        if mo_yr not in data_dict:
            data_dict[mo_yr]

        if mo_yr not in mother_dict:
            mother_dict[mo_yr]

        if mo_yr not in child_dict:
            child_dict[mo_yr]

        data_dict[mo_yr] = [total_participants, preg_women, full_BF_women, partial_BF_women, PP_women, total_women,
                            full_BF_infant, partial_BF_infant, full_formula_infant, total_infants, total_children,
                            admin_money, dshs_source]

        mother_dict[mo_yr] = [total_participants, preg_women, full_BF_women, partial_BF_women, PP_women, total_women]

        child_dict[mo_yr] = [full_BF_infant, partial_BF_infant, full_formula_infant, total_infants, total_children]

        if len(data_dict.keys()) != len(mother_dict.keys()) and len(data_dict.keys()) != len(child_dict.keys()):
            print('Double check data being read. Dictionary month/year keys do not match mother/child dictionary.')
            break

    return data_dict, mother_dict, child_dict


## Run Functions :)

if __name__ == '__main__':
    data_dict, mother_dict, child_dict = read_data(file_path)

