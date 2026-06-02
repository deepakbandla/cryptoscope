import { useState } from 'react';
import { apiClient } from '../services/api';

export default function RsaExplorer() {
    const [bitSize, setBitSize] = useState(256);
    const [keys, setKeys] = useState<any>(null);
    const [loading, setLoading] = useState(false);

    const generateKeys = async () => {
        setLoading(true);
        try {
            const response = await apiClient.post('/rsa/generate', { bit_size: bitSize });
            setKeys(response.data);
        } catch (error) {
            console.error("Failed to generate keys", error);
        }
        setLoading(false);
    };

    return (
        <div className="max-w-4xl">
            <h2 className="text-3xl font-bold text-white mb-2">RSA Mathematics Explorer</h2>
            <p className="text-zinc-400 mb-8">Generate textbook RSA parameters and inspect the modular arithmetic variables.</p>

            <div className="bg-zinc-850 border border-zinc-800 rounded-lg p-6 mb-8">
                <div className="flex items-end gap-4 mb-6">
                    <div>
                        <label className="block text-sm font-medium text-zinc-400 mb-1">Key Bit Size</label>
                        <select
                            value={bitSize}
                            onChange={(e) => setBitSize(Number(e.target.value))}
                            className="bg-zinc-900 border border-zinc-700 text-white rounded px-4 py-2 w-48 focus:outline-none focus:border-blue-500"
                        >
                            <option value={128}>128-bit (Insecure)</option>
                            <option value={256}>256-bit (Textbook)</option>
                            <option value={512}>512-bit (Test)</option>
                        </select>
                    </div>
                    <button
                        onClick={generateKeys}
                        disabled={loading}
                        className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-2 rounded font-medium transition-colors disabled:opacity-50"
                    >
                        {loading ? 'Generating...' : 'Generate Keys'}
                    </button>
                </div>

                {keys && (
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div className="bg-zinc-900 p-4 rounded border border-zinc-800">
                            <span className="text-xs text-zinc-500 uppercase tracking-wider">Public Modulus (n)</span>
                            <p className="text-zinc-300 font-mono text-sm mt-1 break-all">{keys.n}</p>
                        </div>
                        <div className="bg-zinc-900 p-4 rounded border border-zinc-800">
                            <span className="text-xs text-zinc-500 uppercase tracking-wider">Public Exponent (e)</span>
                            <p className="text-zinc-300 font-mono text-sm mt-1">{keys.e}</p>
                        </div>
                        <div className="bg-zinc-900 p-4 rounded border border-zinc-800 md:col-span-2">
                            <span className="text-xs text-red-400 uppercase tracking-wider">Private Exponent (d) - SECRET</span>
                            <p className="text-zinc-300 font-mono text-sm mt-1 break-all">{keys.d}</p>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
}