import {
    LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer
} from 'recharts';

interface PerformanceChartProps {
    data: any[];
}

export default function PerformanceChart({ data }: PerformanceChartProps) {
    if (!data || data.length === 0) {
        return (
            <div className="h-96 w-full mt-4 bg-zinc-900/50 border border-zinc-800 border-dashed rounded flex items-center justify-center text-zinc-500">
                Click 'Execute Benchmark Suite' to generate telemetry graph.
            </div>
        );
    }

    return (
        <div className="h-96 w-full mt-4 bg-zinc-900/50 p-4 rounded border border-zinc-800">
            <ResponsiveContainer width="100%" height="100%">
                <LineChart data={data} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
                    <CartesianGrid strokeDasharray="3 3" stroke="#3f3f46" />
                    <XAxis dataKey="name" stroke="#a1a1aa" />
                    <YAxis stroke="#a1a1aa" />
                    <Tooltip
                        contentStyle={{ backgroundColor: '#18181b', borderColor: '#3f3f46', color: '#fff' }}
                        itemStyle={{ color: '#e4e4e7' }}
                    />
                    <Legend wrapperStyle={{ paddingTop: '20px' }} />
                    <Line type="monotone" dataKey="KeyGen" stroke="#ef4444" strokeWidth={2} activeDot={{ r: 8 }} />
                    <Line type="monotone" dataKey="Encrypt" stroke="#3b82f6" strokeWidth={2} />
                    <Line type="monotone" dataKey="Decrypt" stroke="#10b981" strokeWidth={2} />
                </LineChart>
            </ResponsiveContainer>
        </div>
    );
}