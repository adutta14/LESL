:- consult(syntax).
:- consult(parseTree).
:- initialization syntaxSemantics.

reading(House1) :- open("tokens.lbsl", read, Stream),
    read(Stream, House1).

main() :-
    reading(H), code(H, Rest),length(Rest, Len),
    (   Len > 0
    *-> write("Error")
    ; write("No Error")).

main1(A) :- reading(H), code(A, H, []).

writing(ParseTree) :- open("semantics.txt", write, Stream),
    write(Stream, ParseTree),
    nl(Stream),
    close(Stream).

main2 :- reading(H), code(A, H, []), writing(A).

syntaxSemantics :- reading(H), code(H, Rest1), length(Rest1, Length1),
    (   Length1 > 0
    *-> writing("Error")
    ;   code(A, H, Rest2), length(Rest2, Length2),
        (   Length2 > 0
        *-> writing("Error")
        ;   writing(A))).
