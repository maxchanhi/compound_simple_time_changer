
\version "2.24.1"  
\header {
  tagline = "" \language "english"
}

#(set-global-staff-size 26)

\score {
    \fixed c' {
      \time 12/8
      \omit Score.BarLine
      \tuplet 3/2 {a8 g8 f8} \tuplet 2/3 { a8. b16 } \tuplet 3/2 {e4 a8} \tuplet 3/2 {b8 b8 a8}
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

