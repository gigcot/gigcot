import pandas as pd

# 데이터 로드
file_path = 'D:\\ML_practice_data\\llm_practice2\\clean_df_100.csv'
data = pd.read_csv(file_path)

# 질문-응답 형식 생성 함수
def create_detailed_qa_pairs_by_ingredient(df):
    # 각 주재료를 기준으로 데이터를 전처리
    ingredient_recipes = {}

    for index, row in df.iterrows():
        ingredients = row['CKG_MTRL_CN'].split('|')
        recipe = row['RCP_CONTENT']
        title = row['RCP_TTL']
        servings = row['CKG_INBUN_NM']
        difficulty = row['CKG_DODF_NM']
        dish_type = row['CKG_KND_ACTO_NM']
        method = row['CKG_MTH_ACTO_NM']
        occasion = row['CKG_STA_ACTO_NM']
        
        for ingredient in ingredients:
            ingredient = ingredient.strip()  # 공백 제거
            if ingredient not in ingredient_recipes:
                ingredient_recipes[ingredient] = []
            ingredient_recipes[ingredient].append({
                "title": title,
                "recipe": recipe,
                "servings": servings,
                "difficulty": difficulty,
                "dish_type": dish_type,
                "method": method,
                "occasion": occasion
            })
    
    # 질문-응답 데이터 생성
    qa_pairs = []

    for ingredient, recipes in ingredient_recipes.items():
        if len(recipes) > 1:
            question = f"{ingredient}로 뭘 만들 수 있을까?"
            response_details = []
            for recipe in recipes:
                response_details.append(
                    f"{recipe['title']}: {recipe['recipe']}\n"
                    f"인분: {recipe['servings']}, 난이도: {recipe['difficulty']}, 요리 종류: {recipe['dish_type']}, "
                    f"조리 방법: {recipe['method']}, 상황: {recipe['occasion']}"
                )
            response = '다음과 같은 요리가 있습니다:\n\n' + '\n\n'.join(response_details)
            
            qa_pairs.append({
                "question": question,
                "answer": response
            })
    
    return qa_pairs

# 질문-응답 쌍 생성
qa_data = create_detailed_qa_pairs_by_ingredient(data)

# 결과 미리보기
print(qa_data[:5])

import os

# CSV 파일로 저장
def save_qa_data_to_csv(qa_data, output_file):
    qa_df = pd.DataFrame(qa_data)
    qa_df.to_csv(output_file, index=False, encoding='utf-8-sig')

# 저장할 파일 경로 설정
output_file_path = '../qa_data.csv'

# 데이터 저장
save_qa_data_to_csv(qa_data, output_file_path)

print(f"질문-응답 데이터를 {output_file_path}에 저장했습니다.")
