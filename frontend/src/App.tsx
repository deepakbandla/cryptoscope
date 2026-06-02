import { BrowserRouter as Router, Routes, Route, Link, useLocation } from 'react-router-dom';
import { Shield, Target, Activity, Cpu } from 'lucide-react';
import RsaExplorer from './pages/RsaExplorer';
import AttackSimulator from './pages/AttackSimulator';
import PerformanceResearch from './pages/PerformanceResearch';

const Sidebar = () => {
    const location = useLocation();

    const navItems = [
        { path: '/', name: 'RSA Explorer', icon: <Shield size={20} /> },
        { path: '/attacks', name: 'Cryptanalysis', icon: <Target size={20} /> },
        { path: '/benchmarks', name: 'Telemetry (Phase 5)', icon: <Activity size={20} /> },
    ];

    return (
        <div className="w-64 bg-zinc-950 h-screen border-r border-zinc-800 p-6 flex flex-col fixed">
            <div className="flex items-center gap-3 mb-10 text-white">
                <Cpu size={28} className="text-blue-500" />
                <h1 className="text-xl font-bold tracking-wider">CryptoScope</h1>
            </div>
            <nav className="flex flex-col gap-2">
                {navItems.map((item) => {
                    const isActive = location.pathname === item.path;
                    return (
                        <Link
                            key={item.path}
                            to={item.path}
                            className={`flex items-center gap-3 px-4 py-3 rounded-md transition-colors ${isActive ? 'bg-blue-600/10 text-blue-400' : 'text-zinc-400 hover:bg-zinc-900 hover:text-zinc-200'
                                }`}
                        >
                            {item.icon}
                            <span className="font-medium">{item.name}</span>
                        </Link>
                    );
                })}
            </nav>
        </div>
    );
};

function App() {
    return (
        <Router>
            <div className="flex min-h-screen bg-zinc-900">
                <Sidebar />
                <main className="flex-1 ml-64 p-10">
                    <Routes>
                        <Route path="/" element={<RsaExplorer />} />
                        <Route path="/attacks" element={<AttackSimulator />} />
                        <Route path="/benchmarks" element={<PerformanceResearch />} />
                    </Routes>
                </main>
            </div>
        </Router>
    );
}

export default App;