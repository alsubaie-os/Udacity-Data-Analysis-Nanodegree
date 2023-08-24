# import all packages and set plots to be embedded inline
import pandas as pd


# ----------------------------- Start: Translate columns name to english ----------------------------- #

def column_names_translation(df):
    """
    This function is used to translate the columns names for the given df to english

    Parameters:
    df (DataFrame): dataframe to translate the columns name to english.

    Returns:
    df (DataFrame): dataframe with columns name translated to english.
    """

    df.rename(columns={'السنة': 'year'}, inplace=True)
    df.rename(columns={'الربع': 'quarter'}, inplace=True)
    df.rename(columns={'المنطقة': 'region'}, inplace=True)
    df.rename(columns={'النشاط الاقتصادي': 'sector'}, inplace=True)
    df.rename(columns={'حجم المنشأة': 'enterprise_size'}, inplace=True)
    df.rename(columns={'عدد المنشآت': 'number_of_enterprises'}, inplace=True)
    df.rename(columns={'عدد العاملين السعوديين': 'number_of_saudi_employees'}, inplace=True)
    df.rename(columns={'عدد السعوديين (ذكور)': 'number_of_saudi_employees (male)'}, inplace=True)
    df.rename(columns={'عدد السعوديات (إناث)': 'number_of_saudi_employees (female)'}, inplace=True)
    df.rename(columns={'عدد العاملين الأجانب': 'number_of_foreign_employees'}, inplace=True)
    df.rename(columns={'عدد الأجانب (ذكور)': 'number_of_foreign_employees (male)'}, inplace=True)
    df.rename(columns={'عدد الأجنبيات (إناث)': 'number_of_foreign_employees (female)'}, inplace=True)

    return df


# ----------------------------- End: Translate columns name to english ----------------------------- #


# ----------------------------- Start: Translate the column region values to english ----------------------------- #

# Dictionary contain the translation of the Arabic region to english
translated_region_dict = {
    'المنطقة الشرقية': 'Eastern Province',
    'منطقة الباحة': 'Al Bahah Region',
    'منطقة الجوف': 'Al Jawf Region',
    'منطقة الحدود الشمالية': 'Northern Borders Region',
    'منطقة الرياض': 'Riyadh Region',
    'منطقة القصيم': 'Qassim Region',
    'منطقة المدينة المنورة': 'Al Madinah Region',
    'منطقة تبوك': 'Tabuk Region',
    'منطقة جازان': 'Jazan Region',
    'منطقة حائل': 'Hail Region',
    'منطقة عسير': 'Aseer Region',
    'منطقة مكة المكرمة': 'Makkah Region',
    'منطقة نجران': 'Najran Region'
}


def region_translation(df):
    """
    This function is used to translate the region to english using translated_region_dec dictionary

    Parameters:
    df (DataFrame): dataframe to translate the region to english.

    Return:
    df (DataFrame): dataframe with region translated to english.
    """

    # translate the region to english using translated_region_dec dictionary
    df['region'] = df['region'].apply(lambda x: translated_region_dict[x])

    return df


# ----------------------------- End: Translate the column region values to english ----------------------------- #


# ----------------------------- Start: Translate the column enterprise_size values to english ----------------------------- #

# Dictionary contain the translation of the Arabic enterprise_size to english
translated_enterprise_size_dict = {
    'صغيرة': 'small',
    'كبيرة': 'large',
    'متناهية الصغر': 'micro',
    'متوسطة': 'medium'
}


def enterprise_size_translation(df):
    """
    This function is used to translate the enterprise_size to english using translated_enterprise_size_dec dictionary

    Parameters:
    df (DataFrame): dataframe to translate the enterprise_size to english.

    Return:
    df (DataFrame): dataframe with enterprise_size translated to english.
    """

    # translate the enterprise_size to english using translated_enterprise_size_dec dictionary
    df['enterprise_size'] = df['enterprise_size'].apply(lambda x: translated_enterprise_size_dict[x])

    return df


# ----------------------------- End: Translate the column enterprise_size values to english ----------------------------- #


# ----------------------------- Start: Translate the column sector values to english ----------------------------- #

# Dictionary contain the translation of the Arabic sectors to english
translated_sector_dict = {
    'وكالات السفر ومشغّلو الجولات السياحية وخدمات الحجز والأنشطة المتصلة بها': 'Travel Agencies, Tour Operators, Reservation Services, and Related Activities',
    'صيد الأسماك وتربية المائيات': 'Fishing and Aquaculture',
    'صنع منتجات المعادن المشكلة ( باستثناء الآلات والمعدات )': 'Manufacture of Shaped Metal Products (Except Machinery and Equipment)',
    'صنع منتجات المعادن اللافلزية الأخرى': 'Manufacture of Other Non-Metallic Mineral Products',
    'صنع منتجات المطاط واللدائن': 'Manufacture of Rubber and Plastic Products',
    'صنع فحم الكوك والمنتجات النفطية المكررة': 'Manufacture of Coke and Refined Petroleum Products',
    'صُنع الورق ومنتجات الورق': 'Manufacture of Paper and Paper Products',
    'صُنع المواد الكيميائية والمنتجات الكيميائية': 'Manufacture of Chemicals and Chemical Products',
    'صُنع المنسوجات': 'Manufacture of Textiles',
    'صُنع المنتجات الغذائية': 'Manufacture of Food Products',
    'صنع المنتجات الصيدلانية الأساسية والمستحضرات الصيدلانية': 'Manufacture of Basic Pharmaceuticals and Pharmaceutical Preparations',
    'صُنع المنتجات الجلدية والمنتجات ذات الصلة': 'Manufacture of Leather and Leather Products',
    'صُنع الملبوسات': 'Manufacture of Wearing Apparel',
    'صنع المعدات الكهربائية': 'Manufacture of Electrical Equipment',
    'صُنع المشروبات': 'Manufacture of Beverages',
    'صنع الفلزات القاعدية': 'Manufacture of Basic Metals',
    'صُنع الخشب ومنتجات الخشب والفلين ، باستثناء الأثاث ، صُنع أصناف من القش ومواد الضفر': 'Manufacture of Wood and Wood Products (Except Furniture), Manufacture of Straw and Plaiting Materials',
    'صنع الحواسيب والمنتجات الإلكترونية والبصرية': 'Manufacture of Computers, Electronic and Optical Products',
    'صنع الأثاث': 'Manufacture of Furniture',
    'صناعة معدات النقل الأخرى': 'Manufacture of Other Transport Equipment',
    'صناعة المركبات ذات المحركات والمركبات المقطورة ونصف المقطورة': 'Manufacture of Motor Vehicles, Trailers, and Semi-Trailers',
    'صناعة الآلات والمعدات غير المصنفة في موضع أخر': 'Manufacture of Other Machinery and Equipment Not Classified Elsewhere',
    'توصيل الكهرباء والغاز والبخار وتكييف الهواء': 'Electricity, Gas, Steam, and Air Conditioning Supply',
    'تمويل التأمين وإعادة التأمين وصناديق المعاشات التقاعدية باستثناء الضمان الاجتماعي الإلزامي': 'Activities of Financial Services, Except Mandatory Social Security',
    'تعدين ركازات الفلزات': 'Mining of Metal Ores',
    'تعدين الفحم والليغنيت': 'Mining of Coal and Lignite',
    'تشييد المباني': 'Construction of Buildings',
    'تجميع المياه ومعالجتها وتوصيلها': 'Water Collection, Treatment, and Supply',
    'تجارة الجملة والتجزئة ، وإصلاح المركبات ذات المحركات والدراجات النارية': 'Wholesale and Retail Trade, Repair of Motor Vehicles and Motorcycles',
    'تجارة الجملة ، باستثناء المركبات ذات المحركات والدراجات النارية': 'Wholesale Trade (Except of Motor Vehicles and Motorcycles)',
    'تجارة التجزئة، باستثناء المركبات ذات المحركات والدراجات النارية': 'Retail Trade (Except of Motor Vehicles and Motorcycles)',
    'أنشطة زراعة المحاصيل والإنتاج الحيواني والصيد والخدمات المتصلة': 'Crop and Animal Production, Hunting and Related Services',
    'أنشطة خدمات دعم التعدين': 'Support Services to Mining',
    'أنشطة خدمات المعلومات': 'Information Service Activities',
    'أنشطة خدمات الأطعمة والمشروبات': 'Food and Beverage Service Activities',
    'أنشطة جمع النفايات ومعالجتها وتصريفها ، واسترجاع المواد': 'Waste Collection, Treatment, and Disposal, Materials Recovery',
    'أنشطة تقديم الخدمات للمباني وتجميل المواقع': 'Services to Buildings and Landscape Activities',
    'أنشطة النشر': 'Publishing Activities',
    'أنشطة المنظمات ذات العضوية': 'Activities of Membership Organizations',
    'أنشطة المكتبات والمحفوظات والمتاحف والأنشطة الثقافية الأخرى': 'Libraries, Archives, Museums, and Other Cultural Activities',
    'أنشطة المكاتب الرئيسية، والأنشطة الاستشارية في مجال الإدارة': 'Head Office Activities, Management Consultancy Activities',
    'أنشطة المعمارية والهندسية ، والاختبارات الفنية والتحليل': 'Architectural and Engineering Activities, Technical Testing, and Analysis',
    'أنشطة المعالجة وخدمات إدارة النفايات الأخرى': 'Treatment and Disposal of Non-Hazardous Waste, Other Waste Management Services',
    'أنشطة العمل الاجتماعي، دون إقامة': 'Social Work Activities Without Accommodation',
    'أنشطة الخدمات المالية ، فيما عدا تمويل التأمين وصناديق المعاشات': 'Financial Service Activities, Except Insurance and Pension Funding',
    'أنشطة الخدمات الشخصية الأخرى': 'Other Personal Service Activities',
    'أنشطة التشييد المتخصصة': 'Specialized Construction Activities',
    'أنشطة البريد ونقل الرسائل والطرود بواسطة مندوبين': 'Postal and Courier Activities',
    'أنشطة البرمجة والإذاعة': 'Programming and Broadcasting Activities',
    'أنشطة البرمجة الحاسوبية والخبرة الاستشارية وما يتصل بها من أنشطة': 'Computer Programming, Consultancy, and Related Activities',
    'أنشطة الأمن والتحقيقات': 'Public Order and Safety Activities',
    'أنشطة الاسر المعيشية التي تستخدم أفراداً للعمل المنزلي': 'Activities of Households as Employers of Domestic Personnel',
    'أنشطة الاستخدام': 'Extraction of Natural Gas',
    'الهندسة المدنية': 'Civil Engineering',
    'النقل المائي': 'Water Transport',
    'النقل الجوي': 'Air Transport',
    'النقل البري و النقل عبر الأنابيب': 'Land Transport and Transport Via Pipelines',
    'الطباعة واستنساخ وسائط الأعلام المسجّلة': 'Printing and Reproduction of Recorded Media',
    'الصناعة التحويلية الأخرى': 'Other Manufacturing',
    'الصرف الصحي': 'Sewerage',
    'الصحة البشرية': 'Human Health Activities',
    'الرعاية مع الإقامة': 'Residential Care Activities',
    'الحراجة وقطع الأخشاب': 'Forestry and Logging',
    'التعليم': 'Education',
    'التخزين وأنشطة الدعم للنقل': 'Warehousing and Support Activities for Transportation',
    'البحث والتطوير في المجال العلمي': 'Research and Development in the Physical, Engineering, and Life Sciences',
    'الأنشطة غير المتميزة لإنتاج السلع والخدمات التي تقوم بها الأسر المعيشية الخاصة لإستعمالها الخاص': 'Undifferentiated Goods-Producing Activities of Private Households for Own Use',
    'الأنشطة المهنية والعلمية والتقنية الأخرى': 'Other Professional, Scientific, and Technical Activities',
    'الأنشطة المساعدة لأنشطة الخدمات المالية وأنشطة التأمين': 'Activities Auxiliary to Financial Services and Insurance Activities',
    'الأنشطة القانونية وأنشطة المحاسبة': 'Legal and Accounting Activities',
    'الأنشطة العقارية': 'Real Estate Activities',
    'الأنشطة الرياضية وأنشطة التسلية والترفيه': 'Sports, Entertainment, and Recreation Activities',
    'الأنشطة البيطرية': 'Veterinary Activities',
    'الأنشطة الإيجارية': 'Rental and Leasing Activities',
    'الأنشطة الإدارية للمكاتب ، وأنشطة الدعم للمكاتب وغير ذلك من أنشطة الدعم للأعمال': 'Office Administrative, Office Support, and Other Business Support Activities',
    'الأنشطة الأخرى للتعدين واستغلال المحاجر': 'Other Mining and Quarrying Activities',
    'الأنشطة الإبداعية والفنون وأنشطة الترفيه': 'Creative, Arts, and Entertainment Activities',
    'الإقامة': 'Accommodation',
    'الإدارة العامة والدفاع ؛ والضمان الاجتماعي الإلزامي': 'Public Administration and Defense; Compulsory Social Security',
    'الاتصالات': 'Telecommunications',
    'إصلاح وتركيب الآلات والمعدات': 'Repair and Installation of Machinery and Equipment',
    'إصلاح أجهزة الحاسوب والسلع الشخصية والمنزلية': 'Repair of Computers and Personal and Household Goods',
    'استخراج النفط الخام والغاز الطبيعي': 'Extraction of Crude Petroleum and Natural Gas',
    'أبحاث الإعلان والسوق': 'Advertising and Market Research',
    'غير معرف': 'Unknown'
}


# function to translate the sector to english using translated_sector_dict dictionary
def sector_translation(df):
    """
    Translate the column sector values to english

    Parameters:
    df (DataFrame): The DataFrame to translate the column sector values to english

    Returns:
    df (DataFrame): The DataFrame with the translated column sector values to english
    """

    df['sector'] = df['sector'].apply(lambda x: translated_sector_dict[x])
    return df


# ----------------------------- End: Translate the column sector values to english ----------------------------- #

def main(year, quarters):
    # loop to each quarter file, create dataframe, translate the data to english and append it to the main dataframe
    for quarter in quarters:
        df = pd.read_csv(f"Data/number-of-employees-{year}-q{quarter}.csv")

        # Perform the translation function on the DataFrame
        column_names_translation(df)
        region_translation(df)
        sector_translation(df)
        enterprise_size_translation(df)

        # save the translated dataframe for each quarter
        globals()[f"df_q{quarter}"] = df

    # concatenate the 4 quarters dataframes into one dataframe
    df = pd.concat([df_q1, df_q2, df_q3, df_q4])
    df.reset_index(drop=True, inplace=True)

    # save the concatenated dataframe
    df.to_csv(f"Data/number-of-employees-{year}-english-version.csv", index=False)

    return df


if __name__ == "__main__":
    main()
