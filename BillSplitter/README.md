# 💰 Bill Splitter

Այս ծրագիրը Streamlit-ով ստեղծված պարզ համակարգ է, որը հնարավորություն է տալիս հաշիվների բաշխում կատարել խմբի անդամների միջև։

## 📌 Հատկություններ

- Ավելացնել ծախս՝ նշելով վճարողին, գումարը և մասնակիցներին
- Հաշվարկել յուրաքանչյուրի հաշվեկշիռը
- Հաշվել նվազագույն փոխանցումները՝ պարտքերը մարելու համար

## 🛠 Տեխնոլոգիաներ

- **Python** (հիմնական լոգիկան)
- **Streamlit** (ինտերֆեյսի համար)
- **Collections (defaultdict)** (հաշվեկշիռների համար)

## 🚀 Տեղակայման ուղեցույց

### 1. Պահանջվող փաթեթների տեղակայում

Սկզբում տեղադրեք անհրաժեշտ փաթեթները՝

```bash
pip install streamlit
```

### 2. Ծրագրի գործարկում

```bash
streamlit run app.py
```

## 📜 Օգտագործման եղանակ

1. Մուտքագրեք ծախսը կատարող անձի անունը։
2. Մուտքագրեք գումարը։
3. Մուտքագրեք մասնակիցների անունները (բաժանեք ստորակետով)։
4. Սեղմեք "Ավելացնել ծախս" կոճակը։
5. Ծախսերը ավելացնելուց հետո սեղմեք "Հաշվել պարտքերը" կոճակը՝ հաշվեկշիռներն ու փոխանցումները տեսնելու համար։

## 📝 Օրինակ

Եթե `Անուշը` վճարում է 3000 AMD և այդ գումարը վերաբերում է `Անիին` և `Գևորգին`, ապա հաշվարկվելու է՝

- Անի → Անուշ: 1500 AMD
- Գևորգ → Անուշ: 1500 AMD

## 🔗 Աղբյուրային կոդ

Ծրագրի ամբողջական կոդը կարող եք գտնել ձեր հիմնական ֆայլում bill\_spliter.py

---

✉ **Հարցերի դեպքում** կարող եք կապ հաստատել։ 😊[amalya.pogosyan99@mail.ru]

