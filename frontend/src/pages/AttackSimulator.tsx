import { useState } from 'react';
import { apiClient } from '../services/api';
import { AlertTriangle, Activity } from 'lucide-react';

export default function AttackSimulator() {
    // Pre-fill with our vulnerable modulus (61051 * 61099)
    const [modulus, setModulus] = useState('3730225499');
    const [report, setReport] = useState<any>(null);
    const [loading, setLoading] = useState(false);

    const executeAttack = async () => {
        setLoading(true);
        try {
            const response = await apiClient.post('/attacks/fermat', {
                target_modulus: parseInt(modulus),
                max_iterations: 10000000
            });
            setReport(response.data);
        } catch (error) {
            console.error("Attack failed to execute", error);
        }
        setLoading(false);
    };

    return (
        <div className="max-w-4xl">
            <h2 className="text-3xl font-bold text-white mb-2">Cryptanalysis Sandbox</h2>
            <p className="text-zinc-400 mb-8">Execute Fermat's Factorization to break structurally weak RSA keys.</p>

            <div className="bg-zinc-850 border border-zinc-800 rounded-lg p-6">
                <div className="flex flex-col gap-4 mb-6">
                    <label className="block text-sm font-medium text-zinc-400">Target Public Modulus (n)</label>
                    <div className="flex gap-4">
                        <input
                            type="text"
                            value={modulus}
                            onChange={(e) => setModulus(e.target.value)}
                            className="flex-1 bg-zinc-900 border border-zinc-700 text-white rounded px-4 py-2 font-mono focus:outline-none focus:border-red-500"
                            placeholder="Enter integer n..."
                        />
                        <button
                            onClick={executeAttack}
                            disabled={loading}
                            className="bg-red-900/50 hover:bg-red-900 text-red-200 border border-red-800 px-6 py-2 rounded font-medium transition-colors flex items-center gap-2 disabled:opacity-50"
                        >
                            <AlertTriangle size={18} />
                            {loading ? 'Attacking...' : 'Execute Fermat Attack'}
                        </button>
                    </div>
                </div>

                {report && (
                    <div className="mt-8 border-t border-zinc-800 pt-6">
                        <div className="flex items-center gap-3 mb-4">
                            <Activity className={report.success ? "text-green-500" : "text-yellow-500"} />
                            <h3 className="text-lg font-semibold text-white">
                                {report.success ? 'Attack Successful: Key Factored' : 'Attack Failed: Key Secure'}
                            </h3>
                        </div>

                        <div className="grid grid-cols-2 gap-4 mb-6">
                            <div className="bg-zinc-900 p-4 rounded border border-zinc-800">
                                <span className="text-xs text-zinc-500 uppercase tracking-wider">Execution Time</span>
                                <p className="text-2xl font-bold text-white mt-1">{report.execution_time_ms.toFixed(2)} <span className="text-sm font-normal text-zinc-500">ms</span></p>
                            </div>
                            <div className="bg-zinc-900 p-4 rounded border border-zinc-800">
                                <span className="text-xs text-zinc-500 uppercase tracking-wider">Iterations</span>
                                <p className="text-2xl font-bold text-white mt-1">{report.iterations_executed.toLocaleString()}</p>
                            </div>
                        </div>

                        {report.success && (
                            <div className="bg-green-900/10 border border-green-900/50 rounded p-4 text-green-400 font-mono text-sm break-all">
                                <p>Recovered Prime p = {report.p}</p>
                                <p className="mt-2">Recovered Prime q = {report.q}</p>
                            </div>
                        )}
                    </div>
                )}
            </div>
        </div>
    );
}