def lineup_students(st):
    print(len(st))
    if len(st)==1:
        return []
    else:
        words = st.split(" ")
        grouped_st ={}
        for word in words:
            grouped_st.setdefault(len(word),[]).append(word)
        sorted_grouped_st_key = sorted(grouped_st.items(),key=lambda item:(-item[0]))
        final = []
        for k,v in sorted_grouped_st_key:
            final.append((sorted(v,reverse=True)))
        return [item for subset in final for item in subset]


