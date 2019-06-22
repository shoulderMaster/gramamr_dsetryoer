
class GrammarDestroyer() :


    def __init__(self) :

        # 초성 리스트. 00 ~ 18
        self.CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
        # 중성 리스트. 00 ~ 20
        self.JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
        # 종성 리스트. 00 ~ 27 + 1(1개 없음)
        self.JONGSUNG_LIST = ['', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

        # 초성 리스트. 00 ~ 18
        cho = ['ㄱ', ('ㄱ', 'ㄱ'), 'ㄴ', 'ㄷ', ('ㄷ', 'ㄷ'), 'ㄹ', 'ㅁ', 'ㅂ', ('ㅂ', 'ㅂ'), 'ㅅ', ('ㅅ', 'ㅅ'), 'ㅇ', 'ㅈ', ('ㅈ', 'ㅈ'), ('ㅈ', 'ㅎ'), ('ㄱ','ㅎ'), ('ㄷ', 'ㅎ'), ('ㅂ', 'ㅎ'), 'ㅎ']
        # 중성 리스트. 00 ~ 20
        jung = ['ㅏ', ('ㅏ', 'ㅣ'), ('ㅣ', 'ㅏ'), ('ㅑ', 'ㅣ'), 'ㅓ', ('ㅓ', 'ㅣ'), ('ㅣ', 'ㅓ'), ('ㅕ', 'ㅣ'), 'ㅗ', ('ㅗ', 'ㅏ'), ('ㅗ', 'ㅐ'), ('ㅗ', 'ㅣ'), ('ㅣ', 'ㅗ'), 'ㅜ', ('ㅜ', 'ㅓ'), ('ㅜ', 'ㅔ'), ('ㅜ', 'ㅣ'), ('ㅣ', 'ㅜ'), 'ㅡ', ('ㅡ', 'ㅣ'), 'ㅣ']
        # 종성 리스트. 00 ~ 27 + 1(1개 없음)
        jong = ['', 'ㄱ', 'ㄲ', ('ㄱ', 'ㅅ'), 'ㄴ', ('ㄴ', 'ㅈ'), ('ㄴ', 'ㅎ'), 'ㄷ', 'ㄹ', ('ㄹ', 'ㄱ'), ('ㄹ', 'ㅁ'), ('ㄹ', 'ㅂ'), ('ㄹ', 'ㅅ'), ('ㄹ', 'ㅌ'), ('ㄹ', 'ㅍ'), ('ㄹ', 'ㅎ'), 'ㅁ', 'ㅂ', ('ㅂ', 'ㅅ'), 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
        seperation_list = []
        seperation_list += zip(self.CHOSUNG_LIST, cho)
        seperation_list += zip(self.JUNGSUNG_LIST, jung)
        seperation_list += zip(self.JONGSUNG_LIST, jong)
        seperation_list = [item for item in seperation_list if type(item[1]) is tuple]

        self.seperation_dict = dict(seperation_list)
        print(self.seperation_dict)

    def combined_to_seperated(self, p_ch, previous) :
        if p_ch in self.seperation_dict.keys() :
            pass
            

    def seperate(self, p_ch):
        stride_a = len(self.JUNGSUNG_LIST)*len(self.JONGSUNG_LIST)
        stride_b = len(self.JONGSUNG_LIST)
        if '가' <= p_ch and p_ch <= '힣' :
            ch1 = (ord(p_ch) - ord('가'))//stride_a
            ch2 = ((ord(p_ch) - ord('가')) - stride_a*ch1) // stride_b
            ch3 = (ord(p_ch) - ord('가')) - stride_a*ch1 - stride_b*ch2

            return (self.CHOSUNG_LIST[ch1], self.JUNGSUNG_LIST[ch2], self.JONGSUNG_LIST[ch3])
        else:
            return tuple()

    def combine(p_char_tuple) :
        pass

def main() :
    test = "동해물과 백두산이 마르고 닳도록"
    gd = GrammarDestroyer()
    for i in test :
        print(gd.seperate(i))

main()
