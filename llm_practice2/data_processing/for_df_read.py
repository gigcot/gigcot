import pickle
import pandas as pd
import xml.etree.ElementTree as ET

# 피클 파일 경로
file_path = './clean_df_100.pkl'

# 피클 파일 로드
with open(file_path, 'rb') as file:
    data = pickle.load(file)

# DataFrame 확인
if isinstance(data, pd.DataFrame):
    # DataFrame을 XML로 변환
    def dataframe_to_xml(df, root_tag='root', row_tag='row'):
        root = ET.Element(root_tag)
        for _, row in df.iterrows():
            row_elem = ET.SubElement(root, row_tag)
            for field, value in row.items():
                field_elem = ET.SubElement(row_elem, field)
                field_elem.text = str(value)
        return ET.ElementTree(root)

    # XML로 변환
    xml_tree = dataframe_to_xml(data)

    # XML 파일로 저장
    xml_tree.write('output.xml', encoding='utf-8', xml_declaration=True)

    print("XML 파일로 변환되었습니다.")
else:
    print("데이터는 DataFrame이 아닙니다.")

