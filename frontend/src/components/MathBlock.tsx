import { MathJax } from 'better-react-mathjax';

interface MathBlockProps {
    math: string;
    inline?: boolean;
    className?: string;
}

export default function MathBlock({ math, inline = false, className = '' }: MathBlockProps) {
    // Automatically apply the correct MathJax delimiters
    const formattedMath = inline ? `\\( ${math} \\)` : `\\[ ${math} \\]`;

    return (
        <span className={className}>
            {/* hideUntilTypeset prevents the ugly flash of raw code before rendering */}
            <MathJax hideUntilTypeset={"first"}>
                {formattedMath}
            </MathJax>
        </span>
    );
}