 " " " 
 C o p y r i g h t   ( C )   2 0 1 8   -   R i c k a r d   S j � g r e n 
 " " " 
 i m p o r t   i t e r t o o l s 
 
 i m p o r t   n u m p y   a s   n p 
 
 
 d e f   g s d ( l e v e l s ,   r e d u c t i o n ,   n = 1 ) : 
         " " " 
         C r e a t e   a   G e n e r a l i z e d   S u b s e t   D e s i g n   ( G S D ) . 
 
         P a r a m e t e r s 
         - - - - - - - - - - 
         l e v e l s   :   a r r a y - l i k e 
                 N u m b e r   o f   f a c t o r   l e v e l s   p e r   f a c t o r   i n   d e s i g n . 
         r e d u c t i o n   :   i n t 
                 R e d u c t i o n   f a c t o r   ( b i g g e r   t h a n   1 ) .   L a r g e r   ` r e d u c t i o n `   m e a n s   f e w e r 
                 e x p e r i m e n t s   i n   t h e   d e s i g n   a n d   m o r e   p o s s i b l e   c o m p l e m e n t a r y   d e s i g n s . 
         n   :   i n t 
                 N u m b e r   o f   c o m p l e m e n t a r y   G S D - d e s i g n s   ( d e f a u l t   1 ) .   T h e   c o m p l e m e n t a r y 
                 d e s i g n s   a r e   b a l a n c e d   a n a l o g o u s   t o   f o l d - o v e r   i n   t w o - l e v e l   f r a c t i o n a l 
                 f a c t o r i a l   d e s i g n s . 
 
         R e t u r n s 
         - - - - - - - 
         H   :   2 d - a r r a y   |   l i s t   o f   2 d - a r r a y s 
                 ` n `   m - b y - k   m a t r i c e s   w h e r e   k   i s   t h e   n u m b e r   o f   f a c t o r s   ( e q u a l 
                 t o   t h e   l e n g t h   o f   ` f a c t o r _ l e v e l s ` .   T h e   n u m b e r   o f   r o w s ,   m ,   w i l l 
                 b e   a p p r o x i m a t e l y   e q u a l   t o   t h e   g r a n d   p r o d u c t   o f   t h e   f a c t o r   l e v e l s 
                 d i v i d e d   b y   ` r e d u c t i o n ` . 
 
         R a i s e s 
         - - - - - - 
         V a l u e E r r o r 
                 I f   i n p u t   i s   v a l i d   o r   i f   d e s i g n   c o n s t r u c t i o n   f a i l s .   D e s i g n   c a n   f a i l 
                 i f   ` r e d u c t i o n `   i s   t o o   l a r g e   c o m p a r e d   t o   v a l u e s   o f   ` l e v e l s ` . 
 
         N o t e s 
         - - - - - 
         T h e   G e n e r a l i z e d   S u b s e t   D e s i g n   ( G S D )   [ 1 ] _   o r   g e n e r a l i z e d   f a c t o r i a l   d e s i g n   i s 
         a   g e n e r a l i z a t i o n   o f   t r a d i t i o n a l   f r a c t i o n a l   f a c t o r i a l   d e s i g n s   t o   p r o b l e m s 
         w h e r e   f a c t o r s   c a n   h a v e   m o r e   t h a n   t w o   l e v e l s . 
 
         I n   m a n y   a p p l i c a t i o n   p r o b l e m s   f a c t o r s   c a n   h a v e   c a t e g o r i c a l   o r   q u a n t i t a t i v e 
         f a c t o r s   o n   m o r e   t h a n   t w o   l e v e l s .   P r e v i o u s   r e d u c e d   d e s i g n s   h a v e   n o t   b e e n 
         a b l e   t o   d e a l   w i t h   s u c h   t y p e s   o f   p r o b l e m s .   F u l l   m u l t i - l e v e l   f a c t o r i a l 
         d e s i g n s   c a n   h a n d l e   s u c h   p r o b l e m s   b u t   a r e   h o w e v e r   n o t   e c o n o m i c a l   r e g a r d i n g 
         t h e   n u m b e r   o f   e x p e r i m e n t s . 
 
         N o t e   f o r   c o m m e r c i a l   u s e r s ,   t h e   a p p l i c a t i o n   o f   G S D   t o   t e s t i n g   o f   p r o d u c t 
         c h a r a c t e r i s t i c s   i n   a   p r o c e s s i n g   f a c i l i t y   i s   p a t e n t e d   [ 2 ] _ 
 
         E x a m p l e s 
         - - - - - - - - 
         A n   e x a m p l e   w i t h   t h r e e   f a c t o r s   u s i n g   t h r e e ,   f o u r   a n d 
         s i x   l e v e l s   r e s p e c t i v e l y   r e d u c e d   w i t h   a   f a c t o r   4   : : 
 
                 > > >   g s d ( [ 3 ,   4 ,   6 ] ,   4 ) 
                 a r r a y ( [ [ 0 ,   0 ,   0 ] , 
                               [ 0 ,   0 ,   4 ] , 
                               [ 0 ,   1 ,   1 ] , 
                               [ 0 ,   1 ,   5 ] , 
                               [ 0 ,   2 ,   2 ] , 
                               [ 0 ,   3 ,   3 ] , 
                               [ 1 ,   0 ,   1 ] , 
                               [ 1 ,   0 ,   5 ] , 
                               [ 1 ,   1 ,   2 ] , 
                               [ 1 ,   2 ,   3 ] , 
                               [ 1 ,   3 ,   0 ] , 
                               [ 1 ,   3 ,   4 ] , 
                               [ 2 ,   0 ,   2 ] , 
                               [ 2 ,   1 ,   3 ] , 
                               [ 2 ,   2 ,   0 ] , 
                               [ 2 ,   2 ,   4 ] , 
                               [ 2 ,   3 ,   1 ] , 
                               [ 2 ,   3 ,   5 ] ] ) 
 
         T w o   c o m p l e m e n t a r y   d e s i g n s   w i t h   t w o   f a c t o r s   u s i n g   t h r e e   a n d 
         f o u r   l e v e l s   r e d u c e d   w i t h   a   f a c t o r   2   : : 
 
                 > > >   g s d ( [ 3 ,   4 ] ,   2 ,   n = 2 ) [ 0 ] 
                 a r r a y ( [ [ 0 ,   0 ] , 
                               [ 0 ,   2 ] , 
                               [ 2 ,   0 ] , 
                               [ 2 ,   2 ] , 
                               [ 1 ,   1 ] , 
                               [ 1 ,   3 ] ] ) 
                 > > >   g s d ( [ 3 ,   4 ] ,   2 ,   n = 2 ) [ 1 ] 
                 a r r a y ( [ [ 0 ,   1 ] , 
                               [ 0 ,   3 ] , 
                               [ 2 ,   1 ] , 
                               [ 2 ,   3 ] , 
                               [ 1 ,   0 ] , 
                               [ 1 ,   2 ] ] ) 
 
         I f   d e s i g n   f a i l s   V a l u e E r r o r   i s   r a i s e d   : : 
 
                 > > >   g s d ( [ 2 ,   3 ] ,   5 ) 
                 T r a c e b a c k   ( m o s t   r e c e n t   c a l l   l a s t ) : 
                   . . . 
                 V a l u e E r r o r :   r e d u c t i o n   t o o   l a r g e   c o m p a r e d   t o   f a c t o r   l e v e l s 
 
         R e f e r e n c e s 
         - - - - - - - - - - 
         . .   [ 1 ]   S u r o w i e c ,   I z a b e l l a ,   L u d v i g   V i k s t r � m ,   G u s t a f   H e c t o r ,   E r i k   J o h a n s s o n , 
               C o n n y   V i k s t r � m ,   a n d   J o h a n   T r y g g .    G e n e r a l i z e d   S u b s e t   D e s i g n s   i n 
               A n a l y t i c a l   C h e m i s t r y .    A n a l y t i c a l   C h e m i s t r y   8 9 ,   n o .   1 2   ( J u n e   2 0 ,   2 0 1 7 ) : 
               6 4 9 1  9 7 .   h t t p s : / / d o i . o r g / 1 0 . 1 0 2 1 / a c s . a n a l c h e m . 7 b 0 0 5 0 6 . 
 
         . .   [ 2 ]   V i k s t r � m ,   L u d v i g ,   C o n n y   V i k s t r � m ,   E r i k   J o h a n s s o n ,   a n d   G u s t a f   H e c t o r . 
               C o m p u t e r - i m p l e m e n t e d   s y s t e m s   a n d   m e t h o d s   f o r   g e n e r a t i n g 
               g e n e r a l i z e d   f r a c t i o n a l   d e s i g n s .   U S 9 7 4 6 8 5 0   B 2 ,   f i l e d   M a y   9 , 
               2 0 1 4 ,   a n d   i s s u e d   A u g u s t   2 9 ,   2 0 1 7 .   h t t p : / / w w w . g o o g l e . s e / p a t e n t s / U S 9 7 4 6 8 5 0 . 
 
         " " " 
         t r y : 
                 a s s e r t   a l l ( i s i n s t a n c e ( v ,   i n t )   f o r   v   i n   l e v e l s ) ,   \ 
                         ' l e v e l s   h a s   t o   b e   s e q u e n c e   o f   i n t e g e r s ' 
                 a s s e r t   i s i n s t a n c e ( r e d u c t i o n ,   i n t )   a n d   r e d u c t i o n   >   1 ,   \ 
                         ' r e d u c t i o n   h a s   t o   b e   i n t e g e r   l a r g e r   t h a n   1 ' 
                 a s s e r t   i s i n s t a n c e ( n ,   i n t )   a n d   n   >   0 ,   \ 
                         ' n   h a s   t o   b e   p o s i t i v e   i n t e g e r ' 
         e x c e p t   A s s e r t i o n E r r o r   a s   e : 
                 r a i s e   V a l u e E r r o r ( e ) 
 
         p a r t i t i o n s   =   _ m a k e _ p a r t i t i o n s ( l e v e l s ,   r e d u c t i o n ) 
         l a t i n _ s q u a r e   =   _ m a k e _ l a t i n _ s q u a r e ( r e d u c t i o n ) 
         o r t o g o n a l _ a r r a y s   =   _ m a k e _ o r t h o g o n a l _ a r r a y s ( l a t i n _ s q u a r e ,   l e n ( l e v e l s ) ) 
 
         t r y : 
                 d e s i g n s   =   [ _ m a p _ p a r t i t i o n s _ t o _ d e s i g n ( p a r t i t i o n s ,   o a )   -   1   f o r   o a   i n 
                                       o r t o g o n a l _ a r r a y s ] 
         e x c e p t   V a l u e E r r o r : 
                 r a i s e   V a l u e E r r o r ( ' r e d u c t i o n   t o o   l a r g e   c o m p a r e d   t o   f a c t o r   l e v e l s ' ) 
 
         i f   n   = =   1 : 
                 r e t u r n   d e s i g n s [ 0 ] 
         e l s e : 
                 r e t u r n   d e s i g n s [ : n ] 
 
 
 d e f   _ m a k e _ o r t h o g o n a l _ a r r a y s ( l a t i n _ s q u a r e ,   n _ c o l s ) : 
         " " " 
         A u g m e n t   l a t i n - s q u a r e   t o   t h e   s p e c i f i e d   n u m b e r   o f   c o l u m n s   t o   p r o d u c e 
         a n   o r t h o g o n a l   a r r a y . 
         " " " 
         p   =   l e n ( l a t i n _ s q u a r e ) 
 
         f i r s t _ r o w   =   l a t i n _ s q u a r e [ 0 ] 
         A _ m a t r i c e s   =   [ n p . a r r a y ( [ [ v ] ] )   f o r   v   i n   f i r s t _ r o w ] 
 
         w h i l e   A _ m a t r i c e s [ 0 ] . s h a p e [ 1 ]   <   n _ c o l s : 
                 n e w _ A _ m a t r i c e s   =   l i s t ( ) 
 
                 f o r   i ,   A _ m a t r i x   i n   e n u m e r a t e ( A _ m a t r i c e s ) : 
                         s u b _ a   =   l i s t ( ) 
                         f o r   c o n s t a n t ,   o t h e r _ A   i n   z i p ( f i r s t _ r o w , 
                                                                                   n p . a r r a y ( A _ m a t r i c e s ) [ l a t i n _ s q u a r e [ i ] ] ) : 
                                 c o n s t a n t _ v e c   =   n p . r e p e a t ( c o n s t a n t ,   l e n ( o t h e r _ A ) ) [ : ,   n p . n e w a x i s ] 
                                 c o m b i n e d   =   n p . h s t a c k ( [ c o n s t a n t _ v e c ,   o t h e r _ A ] ) 
                                 s u b _ a . a p p e n d ( c o m b i n e d ) 
 
                         n e w _ A _ m a t r i c e s . a p p e n d ( n p . v s t a c k ( s u b _ a ) ) 
 
                 A _ m a t r i c e s   =   n e w _ A _ m a t r i c e s 
 
                 i f   A _ m a t r i c e s [ 0 ] . s h a p e [ 1 ]   = =   n _ c o l s : 
                         b r e a k 
 
         r e t u r n   A _ m a t r i c e s 
 
 
 d e f   _ m a p _ p a r t i t i o n s _ t o _ d e s i g n ( p a r t i t i o n s ,   o r t o g o n a l _ a r r a y ) : 
         " " " 
         M a p   p a r t i t i o n e d   f a c t o r   t o   f i n a l   d e s i g n   u s i n g   o r t h o g o n a l - a r r a y   p r o d u c e d 
         b y   a u g m e n t i n g   l a t i n   s q u a r e . 
         " " " 
         a s s e r t   l e n ( 
                 p a r t i t i o n s )   = =   o r t o g o n a l _ a r r a y . m a x ( )   +   1   a n d   o r t o g o n a l _ a r r a y . m i n ( )   = =   0 ,   \ 
                 ' O r t h o g o n a l   a r r a y   i n d e x i n g   d o e s   n o t   m a t c h   p a r t i t i o n   s t r u c t u r e ' 
 
         m a p p i n g s   =   l i s t ( ) 
         f o r   r o w   i n   o r t o g o n a l _ a r r a y : 
                 i f   a n y ( n o t   p a r t i t i o n s [ p ] [ f a c t o r ]   f o r   f a c t o r ,   p   i n   e n u m e r a t e ( r o w ) ) : 
                         c o n t i n u e 
 
                 p a r t i t i o n _ s e t s   =   [ p a r t i t i o n s [ p ] [ f a c t o r ]   f o r   f a c t o r ,   p   i n   e n u m e r a t e ( r o w ) ] 
                 m a p p i n g   =   l i s t ( i t e r t o o l s . p r o d u c t ( * p a r t i t i o n _ s e t s ) ) 
                 m a p p i n g s . a p p e n d ( m a p p i n g ) 
 
         r e t u r n   n p . v s t a c k ( m a p p i n g s ) 
 
 
 d e f   _ m a k e _ p a r t i t i o n s ( f a c t o r _ l e v e l s ,   n u m _ p a r t i t i o n s ) : 
         " " " 
         B a l a n c e d   p a r t i t i o n i n g   o f   f a c t o r s . 
         " " " 
         p a r t i t i o n s   =   l i s t ( ) 
         f o r   p a r t i t i o n _ i   i n   r a n g e ( 1 ,   n u m _ p a r t i t i o n s   +   1 ) : 
                 p a r t i t i o n   =   l i s t ( ) 
 
                 f o r   n u m _ l e v e l s   i n   f a c t o r _ l e v e l s : 
                         p a r t   =   l i s t ( ) 
                         f o r   l e v e l _ i   i n   r a n g e ( 1 ,   n u m _ l e v e l s ) : 
                                 i n d e x   =   p a r t i t i o n _ i   +   ( l e v e l _ i   -   1 )   *   n u m _ p a r t i t i o n s 
                                 i f   i n d e x   < =   n u m _ l e v e l s : 
                                         p a r t . a p p e n d ( i n d e x ) 
 
                         p a r t i t i o n . a p p e n d ( p a r t ) 
 
                 p a r t i t i o n s . a p p e n d ( p a r t i t i o n ) 
 
         r e t u r n   p a r t i t i o n s 
 
 
 d e f   _ m a k e _ l a t i n _ s q u a r e ( n ) : 
         n u m b e r s   =   n p . a r a n g e ( n ) 
         l a t i n _ s q u a r e   =   n p . v s t a c k ( [ n p . r o l l ( n u m b e r s ,   - i )   f o r   i   i n   r a n g e ( n ) ] ) 
         r e t u r n   l a t i n _ s q u a r e 
