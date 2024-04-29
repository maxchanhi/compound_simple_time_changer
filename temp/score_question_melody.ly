
\version "2.24.1"  
\header {
  tagline = "" \language "english"
}

#(set-global-staff-size 26)

\score {
    \fixed c' {
      \time 9/8
      \omit Score.BarLine
      \tuplet 2/3 {g8. f16} f8 a4 \tuplet 2/3 {g8. g16}
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


