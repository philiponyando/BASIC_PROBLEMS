
"""

My friend John and I are members of the "Fat to Fit Club (FFC)". John is worried because each month a list with the weights of members is published and each month he is the last on the list which means he is the heaviest.

I am the one who establishes the list so I told him: "Don't worry any more, I will modify the order of the list". It was decided to attribute a "weight" to numbers. The weight of a number will be from now on the sum of its digits.

For example 99 will have "weight" 18, 100 will have "weight" 1 so in the list 100 will come before 99. Given a string with the weights of FFC members in normal order can you give this string ordered by "weights" of these numbers?

Example:
"56 65 74 100 99 68 86 180 90" ordered by numbers weights becomes: "100 180 90 56 65 74 68 86 99"

When two numbers have the same "weight", let us class them as if they were strings and not numbers: 100 is before 180 because its "weight" (1) is less than the one of 180 (9) and 180 is before 90 since, having the same "weight" (9) it comes before as a string.

All numbers in the list are positive numbers and the list can be empty.

Notes
it may happen that the input string have leading, trailing whitespaces and more than a unique whitespace between two consecutive numbers
Don't modify the input
For C: The result is freed.

Sample Tests:
Test.it("Basic tests")
Test.assert_equals(order_weight("103 123 4444 99 2000"), "2000 103 123 4444 99")
Test.assert_equals(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"), "11 11 2000 10003 22 123 1234000 44444444 9999")



ANSWER VARIATIONS:



def order_weight(_str):
    return ' '.join(sorted(sorted(_str.split(' ')), key=lambda x: sum(int(c) for c in x)))
        # sorting is done in 2 successive steps instead of only one  ;)
        # No need for the double sorting, you can do it with a single one by having your anonymous function return a tuple instead of a single value. It will then sort on each item of the tuple in order, i.e.
        # " ".join(sorted(strng.split(), key=lambda x: (sum(int(c) for c in x), x)))




order_weight = lambda s: ' '.join(sorted(sorted(s.split()), key=lambda w: sum(map(int, w))))




def sum_string(s):
    sum = 0
    for digit in s:
        sum += int(digit)
    return sum

def order_weight(strng):
    # your code
    initial_list = sorted(strng.split())
    result = " ".join(sorted(initial_list, key=sum_string))
    
    return result








def weight_key(s):
    return (sum(int(c) for c in s), s)
def order_weight(s):
    return ' '.join(sorted(s.split(' '), key=weight_key))







def order_weight(string):
    return ' '.join(c[1] for c in sorted((sum(int(b) for b in a), a)
                                         for a in string.split()))







def compare_weight(a, b):
    aWeight = sum([int(i) for i in a])
    bWeight = sum([int(i) for i in b])
    return cmp(aWeight, bWeight) or cmp(a, b)
def order_weight(strng):
    n_list = strng.split()
    n_list.sort(compare_weight)
    return ' '.join(n_list)                                         







def order_weight(input):
    input = sorted(input.split())
    output = {}
    for element in input:
        output[element] = sum([int(c) for c in element])
    output = sorted(input, key=output.get)
    print output
    return ' '.join(output)




def order_weight(strng):
    return ' '.join(sorted(sorted(strng.split()), key=lambda w: sum([int(c) for c in w])))




def order_weight(strng):
    return ' '.join(sorted(strng.split(), key=lambda w: (sum(map(int, w)), w)))

"""



#using defaultdict to hold zip()ed keys with >1 values
from collections import defaultdict
def order_weight(strng):
        lstx = []
        dct =defaultdict(list)
        for i in strng.split():
                lstx.append(sum(((int(j)) for j in i )))
        for k,v in sorted(zip(lstx, strng.split())):
                dct[k].append(v)
        return(' '.join([(' '.join(str(e) for e in dct[i]) ) for i in sorted(dct) ]))
    




"""
 Random tests
 Testing for: 17569 8 145147 123 362004 126 264108 54 210192 120 257943 110 10031 5 36969 32 285949 135 496409 160 251480 170 38178 72 233164 164 485206 192 118129 172 170424 194 140864 42 159303 193 329994 179 34931 192 145857 150 49095 23 139510 22 230023 59 399754 185 87
 Testing for: 226781 26 454374 56 472649 112 399190 49 338616 78 339805 196 318655 99 97063 173 112429 78 189636 54 172975 89 132784 130 358611 171 404033 166 317388 110 370976 7 485789 94 26946 46 52777 112 222787 155 322922 48 239303 86 271611 187 364267 179 239362 96 11
 Testing for: 462024 40 459881 167 402574 68 38114 27 406202 119 271224 114 63761 100 6555 116 166596 166 410751 188 255348 59 306612 165 29953 155 114777 156 69902 147 26155 14 443357 116 470070 53 162714 3 1434 78 313355 190 27775 83 3800 197 249348 63 193334 157 46
 Testing for: 60588 64 133805 98 62484 93 279463 189 305903 93 355232 154 24214 41 227655 93 325579 22 311493 170 377794 127 211086 114 88825 148 277809 144 492872 154 81134 174 73246 92 410424 130 401473 5 123016 170 163233 5 90585 68 10950 3 212866 167 330077 9 99
 Testing for: 438124 58 279101 139 5213 2 26347 170 35603 122 315402 110 198928 167 37550 174 392066 13 35229 162 86849 124 168517 140 16087 112 402728 33 81030 184 50792 150 124664 64 381473 64 33372 189 186908 169 175360 81 431041 28 412873 45 153074 97 291649 105 92
 Testing for: 308211 77 447105 87 184431 185 490046 176 474959 24 158198 72 54618 88 418196 136 101075 188 265814 14 480058 100 434269 124 90706 144 149330 188 314946 16 468002 169 420464 195 21082 121 62751 43 173452 11 259579 20 62081 67 342596 96 495427 61 476979 3 66
 Testing for: 258024 68 451083 190 461924 200 237655 56 132597 193 156017 78 447937 69 229088 11 208262 24 68681 175 177562 58 372377 5 433816 36 339142 176 296616 137 43090 120 186817 101 70488 162 186059 163 28697 63 125211 105 43956 123 424728 153 478931 10 226778 116 49
 Testing for: 102645 96 366571 140 25452 30 55129 192 3985 155 210034 199 485068 197 46081 170 321531 59 291882 185 78247 91 101826 121 449586 130 495186 185 32957 189 322331 64 314546 41 449319 190 375385 59 189151 32 139545 25 299870 43 348984 4 412631 121 49825 111 63
 Testing for: 331060 142 29408 27 69635 167 217044 16 146838 3 180308 8 372440 68 241776 72 355776 33 253692 59 403992 19 487584 5 118868 186 281845 143 2153 193 339915 63 464864 135 163069 123 200049 112 352009 85 264661 149 424391 135 160497 194 90647 185 260694 126 64
 Testing for: 163961 112 137450 154 328743 79 147712 133 305144 85 46205 51 296633 103 187620 61 297866 99 121814 151 286473 90 66995 166 33421 113 113234 180 152807 124 210665 125 88960 145 446519 135 278663 12 315195 109 157053 128 249090 154 411353 164 458685 132 103327 45 98
 Testing for: 140650 83 334587 125 320444 13 314108 63 83684 71 373324 130 85031 33 167117 135 475607 95 258568 96 264274 34 234665 13 6123 11 473832 172 258474 112 345166 174 71013 109 340765 73 464936 59 486706 138 407392 185 331773 168 148232 157 110965 53 155642 112 12
 Testing for: 367139 28 357807 97 81164 118 22499 3 195198 81 23083 73 386461 173 478797 78 404388 43 301294 86 164844 130 420284 183 170706 35 220545 77 227601 33 202172 29 383695 42 23164 56 409856 31 56949 31 428222 106 407967 145 411493 90 177539 104 80962 165 85
 Testing for: 58958 82 274618 1 152864 62 289421 139 456166 113 279980 177 365842 107 316297 121 306461 84 352828 106 13626 57 212707 186 196455 144 458046 179 99438 26 1068 72 326711 94 231527 74 56950 107 17070 22 31298 127 6084 76 15708 75 311884 147 408539 164 75
 Testing for: 156939 50 429695 174 212443 150 290825 172 54354 41 288229 25 36803 130 258036 40 87317 120 114178 86 378780 34 165427 72 446421 141 204260 60 297248 173 315894 197 379094 163 101774 52 61861 6 418344 36 111896 97 293829 113 290987 196 304636 111 482020 125 76
 Testing for: 273068 58 476744 4 49410 100 147920 140 96747 107 313340 193 362555 185 26695 155 10956 21 154322 104 193230 117 108618 88 276473 6 91063 189 240945 128 448234 135 272990 13 322280 47 227581 97 45932 16 265 5 237113 114 313889 98 338025 114 327207 156 11
 Testing for: 415400 98 451886 1 171877 131 494451 132 147388 104 329111 101 75087 8 147510 34 363947 41 198685 38 209574 171 30414 172 61856 112 343655 111 319632 67 98158 155 472919 171 470172 176 157374 23 104472 7 472559 125 440851 51 402327 181 39022 3 307656 72 80
 Testing for: 139907 187 402593 115 343131 115 285145 124 324568 196 154201 183 77195 24 459721 190 62430 159 47156 73 434938 65 402942 79 476 60 93418 7 83738 157 123727 37 62567 23 297214 99 338561 148 275907 180 265118 175 44015 60 140654 162 348121 59 44497 78 99
 Testing for: 220310 113 21679 144 111320 172 202912 179 29547 58 34895 35 169605 142 399861 51 285922 73 356467 82 170767 58 464413 49 103505 156 223124 137 271226 130 309470 19 438688 137 215139 172 351188 115 364664 143 67345 90 106425 199 405853 118 137305 127 397803 120 73
 Testing for: 302874 51 407916 13 335848 77 367885 94 19750 177 229544 34 200102 34 266525 64 3671 21 246974 28 377403 62 200102 144 74796 103 300279 122 295115 49 245249 174 143867 143 425847 158 467181 71 252669 184 388717 107 186534 116 498189 67 398895 160 490048 19 94
 Testing for: 443462 141 184891 111 479183 170 140102 143 36333 192 456564 123 313721 173 136755 144 79256 183 126613 122 246285 129 392363 158 47823 41 296356 40 470405 15 227834 144 454044 148 362237 76 75908 22 163870 157 214250 56 92455 65 77577 37 322720 77 183535 140 15
 Testing for: 379481 55 469113 5 251848 179 61118 193 298938 81 264531 158 127965 163 306104 79 378225 20 319048 21 291637 174 88322 79 219631 82 486201 130 72516 77 377078 157 490522 117 378089 18 66926 188 306120 163 126869 19 448625 29 310486 141 262733 73 338859 158 51
 Testing for: 51682 178 153809 186 364141 66 118627 94 160967 87 299801 72 140919 159 346765 77 134104 117 28724 46 273516 147 365884 158 409059 9 254502 100 389408 187 369844 35 453380 138 344449 160 397484 114 44665 83 193639 98 377754 184 262351 186 366881 101 153162 15 49
 Testing for: 410201 41 458253 189 497615 15 59215 51 75388 111 88673 69 293316 60 137602 102 351072 176 174553 14 144052 68 410474 82 107341 143 132969 63 451288 159 420992 80 334280 87 362681 15 480286 102 24295 99 57644 57 257758 83 102440 57 276530 142 263756 41 56
 Testing for: 18884 143 249309 102 442077 40 485350 182 86640 125 351245 42 261903 22 459193 119 170466 112 84955 11 335846 175 174904 55 269139 25 233321 29 290095 169 276303 30 205424 115 31128 161 53380 26 148317 126 225002 93 282385 75 256026 77 255094 178 349376 37 78
 Testing for: 217291 15 552 80 302382 135 350875 118 418737 38 402000 108 239855 17 157557 3 100812 86 492126 68 233980 144 254998 191 288791 130 280484 127 62798 110 469988 85 431615 98 399352 191 165232 163 449144 71 257444 1 295947 105 422833 111 303555 71 122451 54 38
 Testing for: 73255 34 27933 152 381058 175 73403 141 235271 105 220414 34 417276 51 161365 93 15661 8 15181 176 224793 46 113213 22 320360 101 238767 54 453375 44 63899 87 311848 97 85660 111 395624 110 408815 126 236113 99 295257 176 373557 140 4202 5 128620 92 49
 Testing for: 139144 88 182271 59 321915 117 192776 135 160760 9 262423 83 155156 32 498524 120 192655 25 479458 91 339614 194 328009 128 114963 144 391946 183 395133 66 299173 172 288362 177 411703 158 422540 136 143463 127 476976 13 131185 115 223371 88 187565 66 89744 166 80
 Testing for: 153696 45 172647 27 161479 134 24941 32 250923 5 281213 185 439728 95 102907 66 88774 152 129565 3 34681 27 328483 18 155266 44 74160 41 16306 132 439306 76 98902 54 139237 189 96697 17 255560 198 3011 40 182780 60 409447 73 375667 174 79267 33 85
 Testing for: 141656 92 96831 172 295593 127 258209 93 96554 180 100907 199 39340 51 211186 73 243249 53 431932 200 334730 41 311457 35 114995 3 285399 138 253324 89 135502 184 482952 29 379331 199 335580 174 250011 186 468551 82 76848 150 437345 28 452743 72 121994 200 91
 Testing for: 86380 176 99897 196 434733 195 369736 193 465641 181 92907 162 338861 82 180464 70 484232 111 232749 180 397387 39 144145 92 3135 177 107100 178 345938 176 209091 89 54559 188 180778 51 12306 40 324665 59 440930 148 22673 158 294041 150 411629 167 43536 135 99
 Testing for: 177001 182 446403 133 20839 199 66196 38 363611 131 355571 173 15589 25 408326 69 263236 172 50051 133 43985 160 489393 24 454362 133 263898 36 234423 103 453792 66 274734 175 88725 55 100911 57 55433 53 82641 92 41852 167 1727 93 3085 160 276465 169 39
 Testing for: 154801 104 368935 66 480362 145 363415 55 271832 30 43656 97 437568 150 49040 148 459719 61 226976 77 49619 2 402361 146 388517 165 37761 198 319954 166 193794 160 494372 101 10018 3 317298 95 435871 199 443086 18 60679 55 391667 159 124860 106 297953 1 47
 Testing for: 425590 65 345871 154 397485 149 309165 23 442384 40 243060 160 93842 174 138731 93 186322 144 101440 89 337272 134 368476 32 499823 52 465990 153 468828 174 334066 193 105836 177 56800 4 249520 189 487764 26 286405 99 152375 117 426370 122 221687 176 445575 149 4
 Testing for: 366316 200 473864 25 265192 163 427561 127 130063 179 324246 72 1755 169 166785 64 244224 67 464462 167 201058 113 222669 153 60790 34 123729 197 425452 196 475176 63 350049 36 258901 13 187100 149 262220 26 440847 156 369374 146 414889 120 109215 34 316306 105 16
 Testing for: 497926 193 255030 160 295829 200 202930 8 91210 15 119578 32 160594 35 174111 100 269689 24 245585 159 263522 36 257860 162 47990 25 237639 191 205361 200 318106 161 327796 174 273031 93 127948 171 472768 122 425270 24 7083 163 273423 20 48759 94 262239 64 45
 Testing for: 189453 43 430824 152 478363 147 42638 126 44763 98 453706 113 69698 120 110489 196 297930 194 145424 108 155786 120 11389 151 213063 148 104847 156 77418 162 307851 139 440030 171 262823 155 32602 31 236918 152 247591 187 359436 178 463524 164 63624 174 463282 73 9
 Testing for: 305137 177 101060 66 243617 83 220015 172 453290 85 393666 61 460509 96 33187 90 42068 11 470620 114 34438 73 78559 6 323912 185 159405 51 269569 92 341493 132 338960 182 227636 162 443066 166 484523 198 166751 80 384534 174 41002 151 50439 22 470172 106 31
 Testing for: 173271 32 345369 139 145510 141 58072 18 308814 127 413626 130 344411 62 462767 90 401197 82 438695 83 452920 194 160300 46 391061 185 267555 73 385245 123 433283 33 245744 160 205566 87 2627 67 126499 78 305096 35 387104 36 437879 96 255900 17 478490 112 60
 Testing for: 427759 185 299793 113 332941 2 87618 186 317999 70 447474 68 428362 53 115146 105 243374 35 182937 1 232646 78 398461 79 160472 72 218510 64 487178 79 312505 7 452363 84 335878 57 64495 26 322859 119 390264 140 365449 123 441577 65 429418 2 407891 42 9
 Testing for: 339334 42 146818 187 415861 32 161681 62 220863 101 420212 86 347058 76 213676 46 250206 123 347103 107 123949 161 84020 82 312901 22 443347 74 208636 97 440951 68 380202 62 428447 40 448527 24 220832 155 172700 118 324407 133 18955 106 131445 196 184716 118 83
 Testing for: 378721 118 22925 139 206750 41 243506 30 418976 162 380067 102 238414 135 325845 98 192624 99 5666 122 368471 34 116266 31 268211 158 350427 42 289034 109 7616 77 357380 56 404158 57 24135 155 490954 178 220473 71 413638 193 381353 181 344232 159 285604 134 62
 Testing for: 18255 31 497562 19 435561 26 185360 167 399796 2 245 18 435793 15 425647 154 357737 54 342295 81 499439 139 268102 62 123893 153 127712 198 14542 139 350653 13 489859 46 300760 142 289615 60 478699 24 162426 147 306796 98 113354 122 499301 143 185441 198 76
 Testing for: 67413 152 479770 189 497478 85 136067 35 151436 43 301069 14 178585 117 222246 111 149658 166 163287 95 39154 37 91390 82 121283 34 145186 40 19278 13 197877 166 139653 108 223878 169 435486 43 129627 148 332766 175 281011 145 239316 10 4259 133 222174 125 39
 Testing for: 156564 170 25108 150 354463 185 116353 178 304593 122 7219 166 165236 88 183785 86 300289 24 377479 183 94253 80 45715 181 49427 24 386559 26 144631 5 246603 175 345261 39 244996 79 156470 190 275391 8 390030 89 475447 200 218931 106 475108 104 81515 109 73
 Testing for: 204460 112 485069 168 400273 4 475519 179 402263 85 24806 143 356426 49 8055 189 377144 3 62393 119 83830 200 166273 89 336311 17 440152 191 54592 37 340692 44 484481 137 10357 75 492617 44 436737 52 371389 55 40400 27 159563 92 403762 127 379866 127 24
 Testing for: 88728 170 125021 149 458817 112 344489 19 182473 129 408294 86 161525 42 344595 121 89008 15 121480 120 478029 139 238593 154 366243 40 414603 10 393345 152 393025 54 132792 199 383019 46 91856 173 392795 187 265585 72 493619 142 338474 118 123357 142 130439 42 46
 Testing for: 144729 81 171091 6 260675 92 35614 117 21496 147 295756 10 131785 170 35515 8 423578 136 52339 160 126232 98 193550 148 430963 162 246944 121 292302 200 280051 79 369685 178 331001 94 364775 87 55583 136 366550 163 168651 168 252904 128 7400 83 192400 63 20
 Testing for: 327243 131 358090 195 459108 25 263705 198 57307 187 472722 155 463342 18 156889 161 330974 91 384663 5 316326 69 72599 133 373042 84 344269 151 313648 126 370073 41 207552 144 277005 120 70865 117 186548 5 177550 59 199167 161 103469 55 282208 31 375587 136 95
 Testing for: 167341 176 380480 92 62910 84 125958 23 153487 104 11481 148 170202 74 315029 36 120315 139 71550 126 26683 155 311238 180 361791 47 407435 127 101612 128 441231 78 133784 77 280577 8 427804 69 244033 41 72038 182 96157 29 305816 151 117228 10 128681 133 98
 Testing for: 149304 157 495649 199 133445 8 95072 42 335275 158 39610 177 16266 39 375219 106 42300 6 143727 35 493642 28 204192 95 382759 156 446319 139 196846 193 490679 94 418605 125 461412 70 213240 119 59399 114 107441 105 70684 5 8108 100 320242 163 267400 77 19
"""
