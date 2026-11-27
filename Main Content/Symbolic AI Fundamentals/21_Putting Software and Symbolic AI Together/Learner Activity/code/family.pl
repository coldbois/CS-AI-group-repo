% Prolog Family Lab (3.6). Paste into a new Program at swish.swi-prolog.org.

% Facts
parent(john, mary).
parent(mary, alice).

% Rule: X is a grandparent of Y if X is a parent of Z and Z is a parent of Y.
grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

% Queries to try in the query box (type them there, not in this file):
% ?- grandparent(john, alice).
% ?- grandparent(john, Who).
