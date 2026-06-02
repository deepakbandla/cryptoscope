import MathBlock from './MathBlock';

interface KeyValueGridProps {
    label: string;
    value: string | number;
    mathEquation?: string;
    isSecret?: boolean;
    fullWidth?: boolean;
}

export default function KeyValueGrid({
    label,
    value,
    mathEquation,
    isSecret = false,
    fullWidth = false
}: KeyValueGridProps) {

    return (
        <div className={`bg-zinc-900 p-4 rounded border ${isSecret ? 'border-red-900/50' : 'border-zinc-800'} ${fullWidth ? 'md:col-span-2' : ''} relative overflow-hidden`}>
            {isSecret && <div className="absolute top-0 left-0 w-1 h-full bg-red-600"></div>}

            <span className={`text-xs uppercase tracking-wider flex items-center gap-2 ${isSecret ? 'text-red-400' : 'text-zinc-500'}`}>
                {label}
                {mathEquation && <MathBlock math={mathEquation} inline={true} />}
            </span>

            <p className="text-zinc-300 font-mono text-sm mt-3 break-all">{value}</p>
        </div>
    );
}