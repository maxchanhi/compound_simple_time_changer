
\version "2.24.1"  
\header {
  tagline = "" \language "english"
}

#(set-global-staff-size 26)

\score {
    \fixed c' {
      \time 12/8
      \omit Score.BarLine
      a8 g8 f8 a8. b16 e4 a8 b8 b8 a8
    }
    \layout {
      indent = 0\mm
      ragged-right = ##f
      \context {
        \Score
        \remove "Bar_number_engraver"
      }
    }
}


