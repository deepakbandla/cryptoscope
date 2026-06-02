import { useState } from 'react';
import { apiClient } from '../services/api';
import { Activity } from 'lucide-react';
import {
    LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer
} from 'recharts';

export default function PerformanceResearch() {
    const [loading, setLoading] = useState(false);
    const [chartData, setChartData] = useState<any[]>([]);

    const runBenchmark = async () => {
        setLoading(true);
        try {
            // Testing across specific bit sizes to observe exponential scaling
            const response = await apiClient.post('/benchmarks/run', {
                target_dimensions: [64, 128, 256, 512],
                iterations_per_dim: 3
            });

            // Transform backend data for Recharts compatibility
            const formattedData = response.data.data.map((run: any) => ({
                name: `${run.bit_size}-bit`,
                KeyGen: run.metrics.keygen_avg_ms,
                Encrypt: run.metrics.encrypt_avg_ms,
                Decrypt: run.metrics.decrypt_avg_ms,
            }));

            setChartData(formattedData);
        } catch (error) {
            console.error("Benchmark failed", error);
        }
        setLoading(false);
    };

    return (
        <div className="max-w-5xl">
            <h2 className="text-3xl font-bold text-white mb-2">Empirical Profiling Telemetry</h2>
            <p className="text-zinc-400 mb-8">Analyze the asymptotic time complexity of RSA operations across key sizes.</p>

            <div className="bg-zinc-850 border border-zinc-800 rounded-lg p-6 mb-8">
                <div className="flex justify-between items-center mb-8">
                    <div>
                        <h3 className="text-lg font-medium text-zinc-200">Execution Latency (ms) vs. Bit Size</h3>
                        <p className="text-sm text-zinc-500 mt-1">Aggregated mean over 3 iterations to filter OS jitter.</p>
                    </div>
                    <button
                        onClick={runBenchmark}
                        disabled={loading}
                        className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-2 rounded font-medium transition-colors flex items-center gap-2 disabled:opacity-50"
                    >
                        <Activity size={18} />
                        {loading ? 'Running Telemetry...' : 'Execute Benchmark Suite'}
                    </button>
                </div>

                {chartData.length > 0 ? (
                    <div className="h-96 w-full mt-4 bg-zinc-900/50 p-4 rounded border border-zinc-800">
                        <ResponsiveContainer width="100%" height="100%">
                            <LineChart data={chartData} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
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
                ) : (
                    <div className="h-96 w-full mt-4 bg-zinc-900/50 border border-zinc-800 border-dashed rounded flex items-center justify-center text-zinc-500">
                        Click 'Execute Benchmark Suite' to generate telemetry graph.
                    </div>
                )}
            </div>
        </div>
    );
}